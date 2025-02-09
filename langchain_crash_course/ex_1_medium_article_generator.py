import streamlit as st
from langchain_openai import OpenAI, ChatOpenAI
from langchain.prompts import PromptTemplate 
from langchain.chains import LLMChain
from langchain.schema.runnable import RunnablePassthrough, RunnableLambda, RunnableSequence
from langchain_utils import set_chatgpt_env, set_langsmith_env, log_input, log_output

set_chatgpt_env()
set_langsmith_env()

st.title("Medium Article Generator")
topic = st.text_input("Input a topic of interest")
language = st.text_input("Input a language")

title_template = PromptTemplate(
    input_variables=["topic", "language"],
    template="Write a Medium title for an article about {topic} in {language}.",
)

article_template = PromptTemplate(
    input_variables=["title", "language"],
    template="Write a Medium article in {language} based on the {title} and include title at head of article"
             "with title formatted using # and subtitles using ##"
)

llm1 = OpenAI(temperature=0.9)
llm2 = ChatOpenAI(temperature=0.9, model_name='gpt-4') if language.lower() == "english"  or language == "" else llm1

title_sequence = RunnableLambda(log_input) | \
                 RunnableLambda(lambda x: title_template.format(**x)) |  \
                 llm1 | \
                 RunnableLambda(log_output)
article_sequence = RunnableLambda(lambda x: {"title": x, "language": language}) | \
                   RunnableLambda(lambda x: article_template.format(**x)) | \
                   llm2 | \
                   RunnableLambda(log_output)
full_sequence = title_sequence | article_sequence

if topic:
    response = full_sequence.invoke({"topic": topic, "language": language})
    st.write(response.content)