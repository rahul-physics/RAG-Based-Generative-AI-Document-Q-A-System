# 📄 RAG-Based Generative AI Document Q&A System

An advanced **Retrieval-Augmented Generation (RAG)** application that leverages cutting-edge LLM technology for intelligent, document-driven question answering. This system integrates **LangChain**, **Groq's APIs**, **LLaMA 3**, and **Google Embeddings**, deployed through a sleek **Streamlit** interface. It supports **multi-step reasoning** and **real-time query processing** for high-accuracy answers from custom documents.

---

## 🚀 Features

- 🔍 **RAG Architecture**: Combines retrieval and generation to produce accurate, grounded answers from source documents.
- 🤖 **LLM Integration**: Powered by **Groq’s blazing-fast API** with **LLaMA 3** for high-quality natural language understanding.
- 🌐 **Google Embeddings**: Enables efficient document indexing and semantic search.
- 🔄 **LangChain Advanced Chains**: Supports multi-hop reasoning and chained prompt logic.
- 🖥️ **Streamlit Frontend**: Provides an intuitive, interactive interface for uploading documents and querying them in real-time.

---

## 🧠 Tech Stack

- **Python**
- **LangChain**
- **Groq API**
- **LLaMA 3**
- **Google Embeddings**
- **Streamlit**
- **FAISS / ChromaDB** (for vector store management)

---

## 💡 How It Works

1. **Document Upload**: Users upload one or more documents (PDF, TXT, etc.).
2. **Embedding Generation**: Uses Google Embeddings to convert document chunks into vector representations.
3. **Semantic Search**: On query, relevant document sections are retrieved from the vector store.
4. **Answer Generation**: Retrieved context is fed into **LLaMA 3 via Groq API** using LangChain’s prompt templates.
5. **Interactive Display**: The answer is displayed in real-time via Streamlit.

---


