from fastmcp import FastMCP

mcp = FastMCP("tool_server")

@mcp.tool
async def get_products(query: str) -> list[dict]:
    """Retrive list of products from online store"""
    return [{"id": 1, "name": "shoe"}, {"id": 5, "name": "bag"}]

if __name__ == "__main__":
    mcp.run()