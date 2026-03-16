import asyncio
from fastmcp.client import Client


async def main():
    client = Client("./server_return_types.py")

    async with client:
        result = await client.get_prompt(
            "clarification_request",
            {"topic": "deployment strategy"},
        )

        print("\n--- clarification_request ---")
        for msg in result.messages:
            print(f"{msg.role}: {msg.content}")

        result = await client.get_prompt(
            "design_feedback",
            {"component": "authentication flow"},
        )

        print("\n--- design_feedback ---")
        for msg in result.messages:
            print(f"{msg.role}: {msg.content}")

        print("\nMetadata:", result.meta)


if __name__ == "__main__":
    asyncio.run(main())