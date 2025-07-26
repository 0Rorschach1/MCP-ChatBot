"""
Simple chat example using MCPAgent with built-in conversation memory.

This example demonstrates how to use the MCPAgent with its built-in
conversation history capabilities for better contextual interactions.

Special thanks to https://github.com/microsoft/playwright-mcp for the server.
"""

import asyncio
# import mcp_server_time
from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from mcp_use import MCPAgent, MCPClient
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler


async def run_memory_chat():
    """Run a chat using MCPAgent's built-in conversation memory."""
    # Load environment variables for API keys
    load_dotenv()

    # Config file path - change this to your config file
    config_file = "examples/browser_mcp.json"
    config = {
        "mcpServers":
        {
            # "playwright":
            #     {
            #         "command": "npx",
            #         "args": ["@playwright/mcp@latest"]
            #     },

            # "fetch":
            #     {
            #         "command": "uvx",
            #         "args": ["mcp-server-fetch"]
            #     },

            # "zhipu-web-search-sse":
            #     {
            #         "url": "https://open.bigmodel.cn/api/mcp/web_search/sse?Authorization={you ak/sk}"
            #     },

            # "perplexity-ask": # need APIKey
            #     {
            #         "command": "npx",
            #         "args": ["-y", "@chatmcp/server-perplexity-ask"],
            #         "env":
            #             {
            #               "PERPLEXITY_API_KEY": "YOUR_API_KEY_HERE"
            #             }
            #     }

            # "puppeteer":
            #     {
            #         "command": "npx",
            #         "args": ["-y", "@modelcontextprotocol/server-puppeteer"]
            #     },

            # "duckduckgo-search":
            #     {
            #         "command": "npx",
            #         "args": ["-y", "duckduckgo-mcp-server"]
            #     },

            "airbnb":
                {
                    "command": "npx",
                    "args": ["-y", "@openbnb/mcp-server-airbnb", "--ignore-robots-txt"]
                },

            "time":
                {
                    "command": "uvx",
                    "args": ["mcp-server-time", "--local-timezone=America/New_York"]
                },

            "filesystem":
                {
                    "command": "npx",
                    "args": ["-y",  "@modelcontextprotocol/server-filesystem",
                             "C:/Users/V.V/Desktop/", "C:/Users/V.V/Desktop/WWW"]
                },

            # "filesystem":
            #     {
            #         "command": "npx",
            #         "args": ["-y",  "@modelcontextprotocol/server-filesystem",
            #                  "./", "./"]
            #     },

            # "postgres":
            #     {
            #         "command": "docker",
            #         "args": ["run",  "-i",  "--rm",  "mcp/postgres",  "postgresql://host.docker.internal:5432/mydb"]
            #     },

            # "sequential-thinking":
            #     {
            #         "command": "npx",
            #         "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"]
            #     },
        }
    }

    print("Initializing chat...")

    # Create MCP client and agent with memory enabled

    # client = MCPClient.from_config_file(config_file)
    client = MCPClient.from_dict(config)

    # llm = ChatGroq(model="llama-3.3-70b-versatile")
    llm = ChatOllama(model="llama3.1",
                     callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]))


    # Create agent with memory_enabled=True
    agent = MCPAgent(
        llm=llm,
        client=client,
        max_steps=50,
        memory_enabled=True,  # Enable built-in conversation memory
    )

    print("\n===== Interactive MCP Chat =====")
    print("Type 'exit' or 'quit' to end the conversation")
    print("Type 'clear' to clear conversation history")
    print("==================================\n")

    try:
        # Main chat loop
        while True:
            # Get user input
            user_input = input("\nYou: ")

            # Check for exit command
            if user_input.lower() in ["exit", "quit"]:
                print("Ending conversation...")
                break

            # Check for clear history command
            if user_input.lower() == "clear":
                agent.clear_conversation_history()
                print("Conversation history cleared.")
                continue

            # Get response from agent
            print("\nAssistant: ", end="", flush=True)

            try:
                # Run the agent with the user input (memory handling is automatic)
                response = await agent.run(user_input)
                print(response)

            except Exception as e:
                print(f"\nError: {e}")

    finally:
        # Clean up
        if client and client.sessions:
            await client.close_all_sessions()


if __name__ == "__main__":
    asyncio.run(run_memory_chat())
