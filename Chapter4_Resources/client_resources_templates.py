import asyncio
from fastmcp import Client


async def main():
    client = Client("./server_resource_templates.py")

    async with client:

        print("-------------- URI templates --------------\n")

        # Read user summary for first user
        result = await client.read_resource("users://alice/summary")
        print("User alice summary:")
        print(result)
        print()

        # Read user summary for second user
        result = await client.read_resource("users://bob/summary")
        print("User bob summary:")
        print(result)
        print()

        # print("-------------- Wildcard parameters --------------\n")

        # Simple one-segment wildcard
        result = await client.read_resource("logs://auth/error.log")
        print("Auth error log:")
        print(result)
        print()

        # Multi-segment wildcard
        result = await client.read_resource("logs://auth/2024/01/error.log")
        print("Auth dated error log:")
        print(result)
        print()

        # Deeper hierarchy
        result = await client.read_resource(
            "logs://payments/2024/01/15/transactions.log"
        )
        print("Payments transaction log:")
        print(result)
        print()

        # print("-------------- Query parameters --------------\n")

        result = await client.read_resource("greet://alice")
        print(result)
        print()

        result = await client.read_resource("greet://alice?language=es")
        print(result)
        print()

        result = await client.read_resource("greet://bob?language=fr")
        print(result)
        print()


if __name__ == "__main__":
    asyncio.run(main())