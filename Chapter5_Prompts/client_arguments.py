import asyncio
from fastmcp.client import Client


async def main():
    client = Client("./server_arguments.py")

    async with client:
        result = await client.get_prompt(
            "build_search_query",
            {
                "query": "error logs",
                "limit": 5,
            },
        )

        print("\n--- build_search_query ---")
        for msg in result.messages:
            print(f"{msg.role}: {msg.content}")


if __name__ == "__main__":
    asyncio.run(main())