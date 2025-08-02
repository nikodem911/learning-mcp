# server.py
from mcp.server.fastmcp import FastMCP

import asyncio

from grpc_client.blinky_grpc_client import BlinkyClient


async def main():
    # Stateless server (no session persistence, no sse stream with supported client)
    mcp = FastMCP("MCPServer", stateless_http=True, json_response=True)
    blinky_client = BlinkyClient()

    @mcp.tool()
    def turn_led_on(line: int, on: bool) -> str:
        blinky_client.SetLedOn(line, on)
        return "Success"

    @mcp.tool()
    def is_led_on(line: int) -> bool:
        return blinky_client.IsLedOn(line)

    print("Starting MCP server...")
    await mcp.run_streamable_http_async()


if __name__ == "__main__":
    asyncio.run(main())
