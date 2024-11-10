from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

Prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You make a wonderful helper. Please answer the user queries as well"),
        ("user", "Question:{question}")
    ]
)

st.title("Demo Chatbot")
input_text = st.text_input("What do you want to search today ?")

LLM = Ollama(model="llama3.2")
output_parser = StrOutputParser()
chain = Prompt|LLM|output_parser

if input_text:
    st.write(chain.invoke({'question': input_text}))