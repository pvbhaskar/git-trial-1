from mcp.server.fastmcp import FastMCP

mcp = FastMCP("study-prompts")


@mcp.prompt()
def explain_topic(topic: str, level: str = "beginner") -> str:
    """Create a simple explanation prompt for a school topic."""
    return (
        f"Explain the topic '{topic}' for a {level} student. "
        f"Use very simple words, short sentences, and 1 real-life example."
    )


@mcp.prompt()
def make_quiz(topic: str, num_questions: int = 3) -> str:
    """Create a quiz prompt for a school topic."""
    return (
        f"Create a short quiz on '{topic}' with {num_questions} questions. "
        f"Keep the questions easy and include answers at the end."
    )


if __name__ == "__main__":
    mcp.run(transport="stdio")
