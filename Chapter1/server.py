from fastmcp import FastMCP

mcp = FastMCP()

@mcp.tool
def say_hello() -> str:
    """Say hello world"""
    return "Hello World!"

if __name__ == '__main__':
    mcp.run()
