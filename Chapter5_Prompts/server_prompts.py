from fastmcp import FastMCP
from fastmcp.prompts import prompt

mcp = FastMCP()


@mcp.prompt(
    name="write_greeting",
    title="Write Greeting",
    description="Writes a short greeting message.",
    tags={"example", "greeting"},
    meta={"version": "1.0"},
    version=1,
)
async def write_greeting(name: str, tone: str) -> str:
    return f"Write a {tone} greeting for {name}."


class MessagePrompts:
    @prompt(
        name="write_farewell",
        description="Writes a short farewell message.",
        tags={"example", "farewell"},
        version=1,
    )
    def write_farewell(self, name: str) -> str:
        return f"Write a farewell message for {name}."


messages = MessagePrompts()
mcp.add_prompt(messages.write_farewell)

if __name__ == "__main__":
    mcp.run()