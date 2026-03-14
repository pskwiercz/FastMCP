import sys

from fastmcp import FastMCP

def log(msg: str) -> str:
    print(msg, file=sys.stderr, flush=True)

mcp = FastMCP("math_server")

@mcp.tool
def add(a: int, b: int) -> int:
    log(f"add called with {a} and {b}")
    return a + b

if __name__ == '__main__':
    mcp.run()
