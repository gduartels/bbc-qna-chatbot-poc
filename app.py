__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

import streamlit as st
import uuid
from model import rag_chain

from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

if 'session_id' not in st.session_state:
    st.session_state.session_id = None
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'store' not in st.session_state:
    st.session_state.store = {}


def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in st.session_state.store:
        st.session_state.store[session_id] = ChatMessageHistory()
    return st.session_state.store[session_id]

def start_chat():
    session_id = str(uuid.uuid4())
    st.session_state.session_id = session_id

def restart_chat():
    session_id = str(uuid.uuid4())
    st.session_state.session_id = session_id
    st.session_state.messages = []

conversational_rag_chain = RunnableWithMessageHistory(
    rag_chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="chat_history",
    output_messages_key="answer",
)

st.title("BBC Digital - Bot de Atendimento")

if st.session_state.session_id:
    st.sidebar.button('Reiniciar conversa', on_click=restart_chat)
else:
    st.sidebar.button('Iniciar conversa', on_click=start_chat)


if st.session_state.session_id:

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if input := st.chat_input(placeholder = "Digite aqui sua pergunta:"):

        st.session_state.messages.append({"role": "user", "content": input})
        with st.chat_message("user"):
            st.markdown(input)
        
        config = {"configurable": {"session_id": st.session_state.session_id}}
        answer = conversational_rag_chain.invoke(
            {"input": input},
            config=config
        )['answer']

        st.session_state.messages.append({"role": "assistant", "content": answer})
        with st.chat_message("assistant"):
            st.markdown(answer)

        print("Messages")
        print(st.session_state.messages)
        print('\n-------------\n')
        print("Session ID:", st.session_state.session_id)
        print("Session History")
        print(get_session_history(st.session_state.session_id))
        print('\n-------------\n')
