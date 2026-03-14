import asyncio
from fastmcp import Client

async def main():

    client = Client("./server.py")

    async with client:
        print("Connected:", client.is_connected())

        # call known tool
        tools = await client.call_tool("weather_lookup", {"city": "London"})
        print("Tool:", tools.data)

        # read all resources
        rs = await client.list_resources()
        for r in rs:
            content = await client.read_resource(r.uri)
            for block in content:
                print("Resource:", getattr(block, "text", block))

        # call prompt
        p = await client.get_prompt("text_summarization", {"topic": "tutorial"})
        print("Prompt:", p.messages)

    print("Connected after block:", client.is_connected())

    location = Client("./server_location.py")

    async with location:
        c = await location.call_tool("coordinates", {"city": "Paris"})
        print("Location server:", c.data)


if __name__ == "__main__":
    asyncio.run(main())