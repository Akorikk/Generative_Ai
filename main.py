import streamlit as st 
import os 
from groq import Groq
import random 
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os 


load_dotenv()
Grop_api = os.environ["GROQ_API"]

st.set_page_config(
    page_title="Groq Chat Assistant",
    layout="wide",
    initial_sidebar_state="expanded"
)
