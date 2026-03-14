import asyncio
from fastmcp import Client

async def main():
    client = Client("./server.py")

    async with client:
        response = await client.call_tool("say_hello")
        print(response.data)

if __name__ == "__main__":
    asyncio.run(main())