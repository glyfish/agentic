import os

def load_api_key(filepath="../.chatgpt_key"):
    with open(filepath, "r") as file:
        return file.read().strip()


def set_chatgpt_env():
    os.environ["OPENAI_API_KEY"] = load_api_key()


def set_langsmith_env(project_name="pr-crushing-rowing-30", tracing=False):
    os.environ["LANGSMITH_API_KEY"] = load_api_key("../.langsmith_key")
    os.environ["LANGCHAIN_TRACING_V2"] = "true" if tracing else "false"
    os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"
    os.environ["LANGCHAIN_PROJECT"] = "pr-crushing-rowing-30"


def log_input(x):
    print("\n🔍 INPUT DATA:", x)
    return x


def log_output(x):
    print("\n✅ OUTPUT RESULT:", x)
    return x
