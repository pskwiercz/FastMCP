import asyncio
from fastmcp import Client


async def main():
    client = Client("./server_static_resources.py")

    async with client:
        # 1. TextResource
        result = await client.read_resource("resource://hello")
        print(f"\n {result}")

        # 2. BinaryResource
        result = await client.read_resource("resource://binary")
        print(f"\n {result}")

        # 3. FileResource
        result = await client.read_resource("file://example")
        print(f"\n {result}")

        # 5. DirectoryResource
        result = await client.read_resource("resource://data")
        print(f"\n {result}")

        # 4. HttpResource
        result = await client.read_resource("resource://site")
        print(f"\n {result}")


if __name__ == "__main__":
    asyncio.run(main())