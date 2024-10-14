import os
import sys 
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
import keys
from groq import Groq
from langchain.prompts import ChatPromptTemplate

from langchain_groq import ChatGroq

from langchain_core.output_parsers import StrOutputParser


import gradio as gr

def fetch_response(user_input):
    chat = ChatGroq(
        model_name = "mixtral-8x7b-32768",
    )
    
    system = "You are helpful assistance."
    human  = "{text}"

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system",system),("human",human)
        ]
    )
    chain = prompt | chat | StrOutputParser()
    output = chain.invoke({"text":user_input})
    return output
"""
user_input = "Why is ocean formed"
print(fetch_response(user_input))"""

iface =  gr.Interface(
    fn = fetch_response,
    inputs = "text",
    outputs = "text",
    title = "Groq Chatbot",
    description = "Ask a question and get a response"
)

iface.launch()