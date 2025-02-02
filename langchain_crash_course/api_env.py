import os

def load_api_key(filepath="../.chatgpt_key"):
    with open(filepath, "r") as file:
        return file.read().strip()

def set_chatgpt_env():
    os.environ["OPENAI_API_KEY"] = load_api_key()

def set_langsmith_env():
    os.environ["LANGSMITH_API_KEY"] = load_api_key("../.langsmith_key")
    os.environ["LANGCHAIN_TRACING_V2"] = "true"
    os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"
    os.environ["LANGCHAIN_PROJECT"] = "pr-crushing-rowing-30"
