# 📄 Enterprise Document Intelligence System (Agentic RAG)

An AI-powered **Document Intelligence System** that enables users to interact with multiple PDF documents using natural language. Built using **LangChain**, **LangGraph**, **Google Gemini**, **Groq LLMs**, **ChromaDB**, and **Streamlit**, the system leverages an **Agentic Retrieval-Augmented Generation (RAG)** architecture to provide accurate, context-aware responses from unstructured documents.

---

## 🚀 Features

- 📂 Upload and process multiple PDF documents.
- 🔍 Semantic search using vector embeddings.
- 🤖 Agentic RAG pipeline powered by LangChain Agents.
- 🧠 Conversational memory using LangGraph.
- ⚡ Fast inference with Groq LLMs.
- 🌐 Google Gemini embeddings for semantic document retrieval.
- 📑 Intelligent document chunking using Recursive Character Text Splitter.
- 💬 Interactive Streamlit web interface.
- 🎯 Context-aware question answering with reduced hallucinations.
- 🔄 Modular and reusable Python architecture.

---

## 🏗️ System Architecture

```
PDF Documents
      │
      ▼
PyPDFDirectoryLoader
      │
      ▼
RecursiveCharacterTextSplitter
      │
      ▼
Google Generative AI Embeddings
      │
      ▼
Chroma Vector Database
      │
      ▼
Retriever
      │
      ▼
LangChain Agent
      │
      ▼
Groq / Gemini LLM
      │
      ▼
Final Response
```

---

## 🛠️ Tech Stack

### Programming Language
- Python

### Frameworks & Libraries
- LangChain
- LangGraph
- Streamlit

### Large Language Models
- Google Gemini
- Groq LLM

### Embeddings
- Google Generative AI Embeddings

### Vector Database
- ChromaDB

### Document Processing
- PyPDFDirectoryLoader
- RecursiveCharacterTextSplitter

### AI Techniques
- Retrieval-Augmented Generation (RAG)
- Agentic AI
- Semantic Search
- Prompt Engineering
- Vector Embeddings

---

## 📁 Project Structure

```
project/
│
├── app.py                   
├── requirements.txt
└── README.md
```

---

## ⚙️ Workflow

1. Upload one or more PDF documents.
2. Extract document text using **PyPDFDirectoryLoader**.
3. Split documents into semantic chunks.
4. Generate embeddings using **Google Generative AI Embeddings**.
5. Store embeddings inside **ChromaDB**.
6. Retrieve the most relevant document chunks.
7. LangChain Agent determines when and how to retrieve information.
8. Groq or Gemini generates the final context-aware answer.
9. Display responses through the Streamlit interface.

---

## 💡 Key Highlights

- Supports multiple PDF documents.
- Persistent vector database for faster retrieval.
- Agent-based reasoning instead of a simple retrieval chain.
- Modular architecture for easy extension.
- Memory-enabled conversations.
- Optimized chunking strategy for improved retrieval quality.
- Designed to minimize hallucinations by grounding responses in retrieved document context.

---

## 📈 Future Improvements

- Hybrid Search (Vector + BM25)
- Multi-modal document support
- OCR for scanned PDFs
- Citation generation with page references
- User authentication
- Cloud deployment
- Conversation history database
- Support for Word, Excel, and PowerPoint documents

---

## 📚 Technologies Used

- Python
- LangChain
- LangGraph
- Streamlit
- Google Gemini
- Groq
- ChromaDB
- Google Generative AI Embeddings
- PyPDFDirectoryLoader
- RecursiveCharacterTextSplitter

---

## 🎯 Learning Outcomes

Through this project, I gained hands-on experience in:

- Building production-ready Retrieval-Augmented Generation (RAG) systems.
- Developing Agentic AI applications using LangChain Agents.
- Implementing semantic search with vector databases.
- Working with Google Gemini and Groq Large Language Models.
- Document preprocessing and intelligent chunking strategies.
- Prompt engineering for reliable and structured responses.
- Designing scalable and modular AI applications.
- Developing interactive AI applications using Streamlit.

---

## 👨‍💻 Author

**Trailokya Dhotre**
