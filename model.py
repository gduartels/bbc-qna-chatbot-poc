import streamlit as st

from langchain.chains import create_history_aware_retriever, create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_chroma import Chroma
from langchain_community.document_loaders import DirectoryLoader
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

openai_api_key = st.secrets["OPENAI_API_KEY"]

llm = ChatOpenAI(model="gpt-4o-mini", openai_api_key=openai_api_key)
embedding = OpenAIEmbeddings(openai_api_key=openai_api_key)

loader = DirectoryLoader('./md_files/', glob="*.md")
docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
splits = text_splitter.split_documents(docs)
vectorstore = Chroma.from_documents(documents=splits, embedding=embedding)
retriever = vectorstore.as_retriever()

contextualize_q_system_prompt = """
Dado um histórico de chat e a última pergunta do usuário, que pode referenciar o contexto no histórico do chat, formule uma pergunta independente que possa ser compreendida sem o histórico do chat. 
NÃO responda à pergunta, apenas reformule-a se necessário e, caso contrário, devolva-a como está.
"""
contextualize_q_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", contextualize_q_system_prompt),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}"),
    ]
)
history_aware_retriever = create_history_aware_retriever(
    llm, retriever, contextualize_q_prompt
)

qa_system_prompt = """
Você é um assistente para tarefas de perguntas e respostas. 
Use as seguintes partes do contexto recuperado para responder à pergunta. 
Se você não souber a resposta, apenas diga que não sabe. 
Use no máximo cinco frases e mantenha a resposta concisa.

Contexto: {context}"""
qa_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", qa_system_prompt),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}"),
    ]
)
question_answer_chain = create_stuff_documents_chain(llm, qa_prompt)

rag_chain = create_retrieval_chain(history_aware_retriever, question_answer_chain)


