from fastmcp import FastMCP
from mcp.types import Icon

mcp = FastMCP("server-basics")


@mcp.tool(name="find_products",
          description="Retrieve products based on a query.",
          tags={"products", "catalog"},
          icons=[Icon(src="https://upload.wikimedia.org/wikipedia/commons/5/55/Magnifying_glass_icon.svg")],
          meta={"version": "0.5", "author": "catalog-management"},
          )
async def get_products(query: str) -> list[dict]:
    """Function to retrieve available products from an online store"""
    return [{"id": 2, "name": "Shoes"}, {"id": 5, "name": "Jeans"}]


if __name__ == "__main__":
    mcp.run()
