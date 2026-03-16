import asyncio
from fastmcp import Client


async def main():
    client = Client("./server_resource_error.py")

    async with client:

        try:
            result = await client.read_resource("demo://python-error")
            print(result)
        except Exception as e:
            print("Python error resource failed:")
            print(e)
        print()

        try:
            result = await client.read_resource("demo://resource-error")
            print(result)
        except Exception as e:
            print("Resource error resource failed:")
            print(e)
        print()


if __name__ == "__main__":
    asyncio.run(main())