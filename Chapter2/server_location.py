from fastmcp import FastMCP

mcp = FastMCP("server_location")

@mcp.tool
def coordinates(city: str) -> str:
    return f"Coordinates for {city} are: lat=10.0 lon=20.0"

if __name__ == "__main__":
    mcp.run()