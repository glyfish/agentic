# Quickstart: Launch Local LangGraph Server

## Install LangGraph CLI

```sh
pip install --upgrade "langgraph-cli[inmem]"
```

### Create a LangGraph App

Create a new app from the react-agent template. This template is a simple agent that can be flexibly extended to many tools.

```sh
langgraph new apps/app_name --template react-agent-python
```

The options for `--template` are,

1. langgraph-project-python
2. react-agent-python
3. memory-agent-python
4. retrieval-agent-python
5. data-enrichment-agent-js

### Install Dependencies

In the root of your new LangGraph app, install the dependencies in edit mode so your local changes are used by the server:

```sh
pip install -e .
```

### Create a .env file

```sh
LANGSMITH_API_KEY=lsv2...
TAVILY_API_KEY=tvly-...
ANTHROPIC_API_KEY=sk-
OPENAI_API_KEY=sk-...
```

### Launch LangGraph Server

```sh
langgraph dev
```
