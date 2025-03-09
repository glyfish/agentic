import asyncio
from agents.researcher import researcher_agent
from langchain_core.messages import HumanMessage

async def main():
    result = await researcher_agent.ainvoke({
        "messages": [
            HumanMessage(content="Who was Abraham Lincoln?")
        ]
    })
    
    # Get the content from the last message
    response_content = result['messages'][-1].content
    print("Response:", response_content)

if __name__ == "__main__":
    asyncio.run(main()) 