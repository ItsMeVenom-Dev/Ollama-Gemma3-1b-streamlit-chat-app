import os
from dotenv import load_dotenv


from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
load_dotenv()


os.environ['LANGCHAIN_API_KEY']=os.getenv('LANGCHAIN_API_KEY')
os.environ['LANGCHAIN_PROJECT']=os.getenv('LANGCHAIN_PROJECT')
os.environ['LANGCHAIN_TRACING_V2']='true'


prompt=ChatPromptTemplate(
    [
        ('system','you are the intelligent system you have to answer user question according to context'),
        ('user','Question : {question}')
    ]
)

llm=Ollama(model="gemma3:1b")


st.title('Simple App using gemma3')
query=st.chat_input("Enter your quaries:")
output=StrOutputParser()
answer=prompt|llm|output

if query:
    st.write(answer.invoke({"question":query}))
