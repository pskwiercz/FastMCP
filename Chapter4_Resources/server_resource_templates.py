import json
from fastmcp import FastMCP

mcp = FastMCP(name="UserServer")


@mcp.resource("users://{user_id}/summary")
def get_user_summary(user_id: str) -> str:
    """Returns a basic summary for a user."""

    return json.dumps(
        {
            "user_id": user_id,
            "display_name": f"User {user_id}",
            "account_status": "active",
            "plan": "free",
        }
    )


@mcp.resource("logs://{service}/{log_path*}")
def get_log_entry(service: str, log_path: str) -> str:
    """Retrieves log content for a given service and log file path."""

    return json.dumps(
        {
            "service": service,
            "log_path": log_path,
            "message": f"Log data for {service}/{log_path}",
        }
    )


@mcp.resource("greet://{name}{?language}")
def greet(name: str, language: str = "en") -> str:
    """Returns a greeting for a person."""

    if language == "es":
        return f"Hola, {name}"
    if language == "fr":
        return f"Bonjour, {name}"
    return f"Hello, {name}"


if __name__ == "__main__":
    mcp.run()