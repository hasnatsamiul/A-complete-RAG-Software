import streamlit as st
from src.search import RAGSearch

st.set_page_config(page_title="YTRAG Chatbot", page_icon="S")

st.title("Ask anything about Temporal Knowledge Graph (TKG) and Its applications")

@st.cache_resource
def load_rag():
    return RAGSearch()

rag_search = load_rag()

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

query = st.chat_input("Ask something from your documents...")

if query:
    st.session_state.messages.append({"role": "user", "content": query})

    with st.chat_message("user"):
        st.write(query)

    with st.chat_message("assistant"):
        with st.spinner("Searching documents..."):
            answer = rag_search.search_and_summarize(query, top_k=3)
            st.write(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})