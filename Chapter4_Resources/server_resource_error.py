from fastmcp import FastMCP
from fastmcp.exceptions import ResourceError

mcp = FastMCP(name="ErrorDemoServer")


@mcp.resource("demo://python-error")
def python_error() -> str:
    """Demonstrates a standard Python exception."""
    raise ValueError("Something went wrong internally")


@mcp.resource("demo://resource-error")
def resource_error() -> str:
    """Demonstrates a ResourceError with a controlled message."""
    raise ResourceError("Requested item was not found")


if __name__ == "__main__":
    mcp.run()