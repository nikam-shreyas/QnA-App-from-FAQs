import streamlit as st
from langchain_helper import get_chain

st.title("QnA App from FAQS")

question = st.text_input("Question")
chain = get_chain()

if question:  
    response = chain(question)
    st.header("Answer: ")
    st.write(response['result'])
    