import asyncio
from fastmcp import Client

config = {
    "mcpServers": {
        "math": {"command": "python", "args": ["./server_math.py"]},
        "text": {"command": "python", "args": ["./server_text.py"]},
    }
}

async def main():
    client = Client(config)

    async with client:
        result = await client.call_tool(
            "math_add",
            {"a": 3, "b": 5}
        )
        print(result)
        print(result.data)

        result = await client.call_tool(
            "text_greet",
            {"text": "Adam"}
        )
        print(result.data)

if __name__ == "__main__":
    asyncio.run(main())





