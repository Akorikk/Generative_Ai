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

def main():
    st.title("Groq Chat_")

    st.sidebar.title("Select a LLM")
    model = st.sidebar.selectbox(
        "Choose a Model",
        ["llama3-70b-8192", "gemma-7b-it"]
    )

    Conversation_memory = st.sidebar.slider("Conversation Memory length:", 1, 10, 5)

    memory = ConversationBufferWindowMemory(k = Conversation_memory)

    user_question = st.text_area("Ask Your Question")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history=[]
    else:
        for message in st.session_state.chat_history:
            memory.save_context({"input":message["human"]},
                                {"output":message["AI"]})
            

    groq_chat = ChatGroq(
        api_key=Grop_api,
        model_name=model 
    )

    conversation = ConversationChain(
        llm=groq_chat,
        memory=memory
    ) 


    if user_question:
        response = conversation(user_question)
        message = {"human":user_question, "AI":response["response"]}
        st.session_state.chat_history.append(message)
        st.write("Chatbot:", response["response"])

if __name__== "__main__":
    main()
