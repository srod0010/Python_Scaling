"""Annotated example of one research agent with switchable output styles.

This consolidates multiple overlapping snippets into one cleaner pattern:
- One shared research behavior
- One place to define style-specific output rules
- One async function to run a research request
- One interactive CLI loop for trying different formats

Before running:
- Install the SDK that provides the `agents` module
- Ensure any required API credentials are set in your shell
"""

import asyncio

try:
    from agents import Agent, Runner, WebSearchTool
except ModuleNotFoundError as exc:
    raise SystemExit(
        "Missing dependency: install the OpenAI Agents SDK with "
        "`pip install openai-agents`, then rerun this script."
    ) from exc


# Shared research rules that apply regardless of output format.
BASE_INSTRUCTIONS = """
You are a professional research assistant.

When given a topic to research:
1. Search for current, reliable information.
2. Prioritize authoritative and recent sources.
3. Synthesize findings instead of repeating raw search results.
4. Include specific facts, dates, and notable developments when available.
5. Cite sources when possible.
6. If information is uncertain or conflicting, say so clearly.
""".strip()


# Style-specific formatting rules. This keeps the prompt logic centralized.
STYLE_INSTRUCTIONS = {
    "bullets": """
Format the final answer as a concise, scannable bullet-point summary.

Rules:
1. Use 8 to 12 bullets maximum.
2. Each bullet should be one complete thought.
3. Lead each bullet with a concrete insight, action, or fact.
4. Keep the response easy to skim.

Use this structure:
# Research Summary: [Topic]

## Key Findings
- [Important finding]
- [Important finding]

## Current Developments
- [Recent update]
- [Recent update]

## Important Facts
- [Specific data point or source-backed fact]
- [Specific data point or source-backed fact]
""".strip(),
    "paragraphs": """
Format the final answer as a compact narrative report.

Rules:
1. Write no more than 3 paragraphs.
2. Each paragraph should cover a distinct aspect of the topic.
3. Use smooth transitions between sections.
4. Include concrete details, dates, and examples.

Use this structure:
# Research Report: [Topic]

**Overview:** [First paragraph]

**Current State:** [Second paragraph]

**Implications:** [Third paragraph]
""".strip(),
}


def build_research_agent(style="bullets"):
    """Create a research agent whose output format depends on the chosen style."""
    if style not in STYLE_INSTRUCTIONS:
        valid_styles = ", ".join(sorted(STYLE_INSTRUCTIONS))
        raise ValueError(f"Unsupported style '{style}'. Choose from: {valid_styles}")

    # Combine shared research behavior with the requested output format.
    instructions = f"{BASE_INSTRUCTIONS}\n\n{STYLE_INSTRUCTIONS[style]}"

    return Agent(
        name=f"Research Assistant ({style})",
        instructions=instructions,
        tools=[WebSearchTool()],
    )


async def research_topic(topic, style="bullets"):
    """Run one research task and return the agent's final formatted answer."""
    agent = build_research_agent(style)

    # The task prompt is intentionally short because the formatting rules already
    # live inside the agent instructions.
    result = await Runner.run(agent, f"Research this topic: {topic}")
    return result.final_output


async def interactive_research():
    """Simple CLI loop to try the same research workflow with different styles."""
    print("Research Assistant")
    print("Available styles: bullets, paragraphs")
    print("Type 'quit' to exit.\n")

    while True:
        topic = input("Topic: ").strip()
        if topic.lower() in {"quit", "exit", "q"}:
            print("Exiting.")
            break

        if not topic:
            print("Enter a topic.\n")
            continue

        style = input("Style (bullets/paragraphs): ").strip().lower() or "bullets"
        if style not in STYLE_INSTRUCTIONS:
            print("Invalid style. Choose 'bullets' or 'paragraphs'.\n")
            continue

        print("\n" + ("=" * 60))
        try:
            output = await research_topic(topic, style)
            print(output)
        except Exception as exc:
            # Keep error handling visible in the example so it is easier to adapt.
            print(f"Research failed: {exc}")
        print("=" * 60 + "\n")


async def compare_styles(topic):
    """Run the same topic twice so you can compare both output formats."""
    for style in ("bullets", "paragraphs"):
        print(f"\n{style.upper()}".center(60, "="))
        try:
            output = await research_topic(topic, style)
            print(output)
        except Exception as exc:
            print(f"Research failed for style '{style}': {exc}")
    print("\n" + ("=" * 60))


if __name__ == "__main__":
    # Default entry point: interactive mode.
    asyncio.run(interactive_research())

    # Alternative:
    # asyncio.run(compare_styles("renewable energy storage technologies"))
