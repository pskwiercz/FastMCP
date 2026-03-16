import asyncio
from fastmcp import Client
import base64


async def main():
    client = Client("./server_dynamic_resources.py")

    async with client:
        result = await client.read_resource("data://active-connections")
        print(result)
        print()

        result = await client.read_resource("data://server-time")
        print(result)
        print()

        bytes_result = await client.read_resource("data://welcome-bytes")
        print(bytes_result)
        blob = bytes_result[0].blob
        print("Welcome bytes resource (raw):")
        print(blob)
        print()

        print("Welcome bytes decoded:")
        print(base64.b64decode(blob))


if __name__ == "__main__":
    asyncio.run(main())