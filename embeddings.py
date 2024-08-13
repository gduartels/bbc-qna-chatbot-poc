import streamlit as st
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores.chroma import Chroma

openai_api_key = st.secrets["OPENAI_API_KEY"]

embedding = OpenAIEmbeddings(openai_api_key=openai_api_key)

loader = DirectoryLoader('./md_files/', glob="*.md")
docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
splits = text_splitter.split_documents(docs)

persist_dir = 'Embedding'
vectordb = Chroma.from_documents(documents=splits, embedding=embedding,
                                    persist_directory=persist_dir)
vectordb.persist()