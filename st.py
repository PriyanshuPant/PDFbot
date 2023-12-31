# Frontend.py
from http.client import HTTPException

import streamlit as st
from pathlib import Path
from dotenv import load_dotenv
from PDF_reader import PDF_reader
from openai import OpenAI
from openai import OpenAIError

from BOT import BOT
from PDF_reader import PDF_reader


bot = BOT()
# from langchain.chat_models import ChatOpenAI
# from langchain.chains import ConversationalRetrievalChain
# from langchain.memory import ConversationBufferMemory
# from langchain.vectorstores import FAISS

pdf = None
load_dotenv()

st.header("AstroPDF 💬")
user_question = st.text_input("Ask a question about your documents:")

with st.sidebar:
    st.subheader("Your documents")
    pdf_docs = st.file_uploader(
            "Upload your PDFs here'",
        accept_multiple_files=False
        )

    if pdf_docs:
        with st.spinner('Processing'):

             pdf = PDF_reader(pdf_docs)





if st.button("Ask"):
    if pdf is not None:
        chunk, page_no = pdf.get_relevant_chunks(user_question)
        response = bot.answer(user_question, chunk, page_no)[0]
        st.write(response)


