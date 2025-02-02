import os
import streamlit as st
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate 
from langchain.chains import LLMChain

f = open("../.chatgpt_key", "r")
api_key = f.read().rstrip()

os.environ["OPENAI_API_KEY"] = api_key

st.title("Medium Article Generator")
topic = st.text_input("Input a topic of interest")
language = st.text_input("Input a language")

title_template = PromptTemplate(
    input_variables=["topic", "language"],
    template="Write a Medium title for an article about {topic} in {language}.",
)

llm = OpenAI(temperature=0.9)
title_chin = LLMChain(llm=llm, prompt=title_template)

if topic:
    response = title_chin.invoke({"topic": topic, "language": language})
    st.write(response["text"])