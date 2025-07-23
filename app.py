# app.py

import streamlit as st
import os
from coordinator import process_document_and_query

st.set_page_config(page_title="Agentic RAG Chatbot", layout="wide")
st.title("📄 Agentic RAG Chatbot")

uploaded_file = st.file_uploader("Upload document", type=["pdf", "docx", "txt", "csv", "pptx", "md"])

if uploaded_file:
    file_path = os.path.join("data", uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())

    query = st.text_input("Ask a question about the document")

    if query and st.button("Get Answer"):
        response = process_document_and_query(file_path, query)
        st.markdown("### 🧠 Answer:")
        st.success(response["payload"]["answer"])
