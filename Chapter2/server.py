from fastmcp import FastMCP
from mcp.types import Icon

mcp = FastMCP(
    name="server-basics",
    instructions="Use this server to get weather information for a specific city",
    version="0.1",
    icons=[
        Icon(
            src="https://commons.wikimedia.org/wiki/Category:Weather_icons#/media/File:Crystal_Project_kweather.png"
        )
    ],
    website_url="website.com",
)


@mcp.tool
async def weather_lookup(city: str) -> str:
    """Returns the current weather in the specified city"""
    return f"The current weather in {city} is cloudy with a chance of meatballs"


@mcp.resource("resource://docs")
async def server_documentation() -> str:
    """Provides basic built-in documentation from the server."""
    return "The basic FactMCP server can expose tools, resources, and prompts."


@mcp.prompt
async def text_summarization(topic: str) -> str:
    """Generic template hosted on the server that any client could use."""
    return f"Write a three-sentence summary about: {topic}"


if __name__ == "__main__":
    mcp.run()