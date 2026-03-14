import sys
from fastmcp import FastMCP

def log(msg: str) -> str:
    print(msg, file=sys.stderr, flush=True)

mcp = FastMCP("text_server")

@mcp.tool
def greet(text: str) -> str:
    log(f"greet colled with {text}")
    return text.upper()

if __name__ == '__main__':
    mcp.run()