from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st 
import os

load_dotenv()

# Set your Gemini API key
os.environ["GOOGLE_API_KEY"] = 'AIzaSyC0WJi0DOIvmOeSnUrhcI4xNbgUP4X0gMU'




## Prompt Template

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please response to the user queries"),
        ("user","Question:{question}")
    ]
)


## streamlit framework

st.title('Langchain Demo With Gemini')
input_text=st.text_input("Search the topic u want")


#model
model = ChatGoogleGenerativeAI(model='gemini-1.5-pro')
parser = StrOutputParser()
chain = prompt | model | parser

if input_text:
    st.write(chain.invoke({'question':input_text}))