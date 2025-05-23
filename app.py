import streamlit as st
import os
from langchain_groq import ChatGroq
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings

from dotenv import load_dotenv

load_dotenv()
groq_api_key = os.getenv('GROQ_API_KEY')
gemini_api_key = os.getenv("GEMINI_API_KEY")

st.title("Gen Ai Document Q&A")
llm=ChatGroq(groq_api_key=groq_api_key, model_name="Llama3-8b-8192")

prompt=ChatPromptTemplate.from_template(
"""
Answer the question based on the provided context only.
Please provide the accurate response based on the question
<context>
{context}
<context>
question:{input}
""")

def vector_embedding():
    if "vectors" not in st.session_state:
        st.session_state.embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004",google_api_key=gemini_api_key)
        st.session_state.loader=PyPDFDirectoryLoader("./journal")
        st.session_state.docs=st.session_state.loader.load()
        st.session_state.text_splitter=RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        st.session_state.final_document=st.session_state.text_splitter.split_documents(st.session_state.docs)
        st.session_state.vectors=FAISS.from_documents( st.session_state.final_document,st.session_state.embeddings)


prompt1=st.text_input("Enter your question:")

if st.button("generate vectore store"):
    vector_embedding()
    st.write("My vector store is created")

import time

if prompt1:
    document_chain= create_stuff_documents_chain(llm,prompt)
    retriever=st.session_state.vectors.as_retriever()
    retriver_chain=create_retrieval_chain(retriever,document_chain)
    start=time.process_time()

    response=retriver_chain.invoke({"input":prompt1})
    st.write(response['answer'])

    with st.expander("Document Simillarity Search"):
        for i,doc in enumerate(response['context']):
            st.write(doc.page_content)
            st.write('--------------')








