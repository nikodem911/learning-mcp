# server.py
from mcp.server.fastmcp import FastMCP

# Stateless server (no session persistence, no sse stream with supported client)
mcp = FastMCP("StatelessServer", stateless_http=True, json_response=True)

# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers and add 10 for debugging"""
    print(f"Adding {a} and {b}")
    return a + b + 10


# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"


print("Starting MCP server...")
mcp.run(transport="streamable-http")