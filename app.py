from dotenv import load_dotenv
load_dotenv()


import warnings
warnings.filterwarnings("ignore")

from langchain_community.document_loaders import PyPDFLoader, PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_chroma import Chroma
from langchain.agents import create_agent
from langchain_core.prompts import ChatPromptTemplate
from langchain.tools import tool
from langgraph.checkpoint.memory import InMemorySaver
from langchain_groq import ChatGroq
import streamlit as st



if "document_uploaded" not in st.session_state:
    st.session_state.document_uploaded = False
    
if "agent" not in st.session_state:
    st.session_state.agent = None
    
if "vector_store" not in st.session_state:
    st.session_state.vector_store = None
    
if "messages" not in st.session_state:
    st.session_state.messages =[]   
    

def process_document(path):
    
    # loading Documnent 
    loader = PyPDFDirectoryLoader(path)
    docs = loader.load()
        
    # splitting docs in chunks    
    splitter = RecursiveCharacterTextSplitter(chunk_size = 1000, chunk_overlap = 200)
    chunks = splitter.split_documents(documents = docs)
            
    # defining Vectore Database
    embedding = GoogleGenerativeAIEmbeddings(model = "gemini-embedding-2")
    vectore_database = Chroma.from_documents(
        documents=chunks,
        embedding=embedding
    )

    @tool
    def retriver(query:str):
        
        """this tool is can help you to retrive the relevent data of the pdf cocumnet and these pdf document 
        have details about medical report
        """
        
        docs = vectore_database.similarity_search(query = query, k = 2)
        context = " "
        for doc in docs:
            context += doc.page_content + "\n"
            
        return context


    llm = ChatGoogleGenerativeAI(model = "gemini-3.5-flash")
    
    # llm = ChatGroq(
    # model="llama-3.3-70b-versatile",
    # temperature=0,
    # max_retries=2,
    # )
    
    system_prompt = """
    your are the helpfull assistant that answer the question using retrived context,
    ALWAYS use "retriver_tool" tool to question requiring external data
    """

    memory = InMemorySaver()


    agent = create_agent(
        model= llm,
        tools= [retriver],
        system_prompt=system_prompt,
        checkpointer=memory
    )
    
    st.session_state.agent = agent
    st.session_state.document_uploaded = True
     
     
            
## upload UI
if not st.session_state.document_uploaded:
    uploaded = st.file_uploader(label="Select PDF Files", type=["pdf"], accept_multiple_files=True)
    if uploaded:
        with st.spinner("Processing..."):
            path = "./doc_file/"
            for file in uploaded:
                with open(path + file.name, "wb") as f:
                    f.write(file.getvalue())

            process_document(path)
            st.rerun()


    
## Chat UI
if st.session_state.document_uploaded and  st.session_state.agent:
    for message in st.session_state.messages:
        role = message["role"]
        content = message["content"]
        st.chat_message(role).markdown(content)
        
    query = st.chat_input("Ask Anything About Documnet: ")
    
    if query:
        
        st.session_state.messages.append({"role":"user","content":query})
        st.chat_message("user").markdown(query)
        
        response = st.session_state.agent.invoke(
            {"messages":[{"role":"user","content":query}]},
            {"configurable":{"thread_id":"1"}}
        )
        result = response["messages"][-1].content[0]["text"]
        
        st.chat_message("ai").markdown(result)
        st.session_state.messages.append({"role":"ai","content":result})
        
    
    

