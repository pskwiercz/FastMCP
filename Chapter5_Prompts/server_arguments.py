from fastmcp import FastMCP
from fastmcp.prompts import Message, PromptResult

mcp = FastMCP(name="DemoPromptServer")


@mcp.prompt
def build_search_query(
    query: str,
    limit: int = 10,
    include_archived: bool = False,
) -> str:
    """Builds a search request with optional parameters."""
    return (
        f"Search for '{query}' with a limit of {limit}. "
        f"Include archived results: {include_archived}."
    )


if __name__ == "__main__":
    mcp.run()