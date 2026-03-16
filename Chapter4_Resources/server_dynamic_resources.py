from fastmcp import FastMCP
import json
import time

mcp = FastMCP(name="TimeServer")


@mcp.resource(uri="data://active-connections")
async def get_active_connections() -> str:
    """
    Returns the number of active client connections.
    Simple integer resource.
    """
    return "15"


@mcp.resource(
    uri="data://server-time",
    name="ServerTime",
    description="Provides the current server time and timezone.",
    mime_type="application/json",
    tags={"time", "system"},
    meta={"format": "unix+iso"},
)
async def get_server_time() -> str:
    """Provides the current server time and timezone"""

    return json.dumps(
        {
            "unix_timestamp": int(time.time()),
            "iso_time": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "timezone": "UTC",
        }
    )


@mcp.resource(uri="data://welcome-bytes")
async def get_welcome_bytes() -> bytes:
    """
    Returns a short welcome message as raw bytes.
    Demonstrates a simple binary resource.
    """
    return b"Welcome to the TimeServer"


if __name__ == "__main__":
    mcp.run()