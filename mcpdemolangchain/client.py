import asyncio
from dotenv import load_dotenv

from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_groq import ChatGroq
from langchain.agents import create_agent

load_dotenv()


async def main():

    client = MultiServerMCPClient(
        {
            "math": {
                "command": "python",
                "args": ["mathserver.py"],
                "transport": "stdio",
            },
            "weather": {
                "url": "http://localhost:8000/mcp",
                "transport": "streamable_http",
            },
        }
    )

    tools = await client.get_tools()

    print("\nLoaded tools:")
    for tool in tools:
        print("-", tool.name)

    model = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0,
    )

    agent = create_agent(
        model=model,
        tools=tools,
    )

    response = await agent.ainvoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": "What is 3 plus 5?"
                }
            ],
            "messages": [
                {
                    "role": "user",
                    "content": "What is weather in new delhi ?"
                }
            ]
        }
    )

    print("\nResponse:")
    print(response["messages"][-1].content)


if __name__ == "__main__":
    asyncio.run(main())