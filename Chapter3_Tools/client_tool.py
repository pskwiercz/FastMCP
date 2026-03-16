import asyncio
from  fastmcp import Client

client = Client("./server_tool.py")

async def main():
    async with client:
        response = await client.call_tool("get_products",
                                          {"query": ""})
        print(response.structured_content)

if __name__ == "__main__":
    asyncio.run(main())

