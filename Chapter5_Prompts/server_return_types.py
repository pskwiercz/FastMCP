from fastmcp import FastMCP
from fastmcp.prompts import Message, PromptResult

mcp = FastMCP(name="DemoPromptServer")


@mcp.prompt
def clarification_request(topic: str) -> list[Message]:
    """Asks the user to clarify a topic."""
    return [
        Message(
            f"Can you clarify what you mean by '{topic}'? "
            "Please include context and constraints."
        )
    ]


@mcp.prompt
def design_feedback(component: str) -> PromptResult:
    """Requests structured design feedback."""
    return PromptResult(
        messages=[
            Message(
                f"Provide design feedback for the component '{component}'. "
                "Focus on usability and maintainability."
            ),
            Message(
                "I will analyze the design and give detailed feedback.",
                role="assistant",
            ),
        ],
        meta={
            "category": "design-review",
            "priority": "medium",
        },
    )


if __name__ == "__main__":
    mcp.run()