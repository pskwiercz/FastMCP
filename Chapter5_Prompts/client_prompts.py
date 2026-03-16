import asyncio
from fastmcp import Client


async def main():
    client = Client("./server_prompts.py")

    async with client:
        greeting = await client.get_prompt(
            "write_greeting",
            {
                "name": "Alex",
                "tone": "casual",
            },
        )
        print(greeting)

        print()
        farewell = await client.get_prompt(
            "write_farewell",
            {
                "name": "Alex",
            },
        )
        print(farewell)


if __name__ == "__main__":
    asyncio.run(main())