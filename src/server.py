# server.py
from mcp.server.fastmcp import FastMCP

import asyncio
import random
import string

async def main():
    # Stateless server (no session persistence, no sse stream with supported client)
    mcp = FastMCP("MCPServer", stateless_http=True, json_response=True)
    
    @mcp.tool()
    def book_flight(from_: str, to: str, departure_date: str) -> str:
        """Book a flight and return a booking reference.

        Parameters:
            from_ (str): Origin airport or city (IATA code or human-readable name).
            to (str): Destination airport or city (IATA code or human-readable name).
            departure_date (str): Departure date in YYYY-MM-DD format.

        Returns:
            str: Booking reference code (opaque string), e.g. "RUDYTS".
        """
        
        print(f"Booking flight from {from_} to {to} on {departure_date}")

        # Return random 6-character uppercase booking reference
        confirmation_code = ''.join(random.choices(string.ascii_uppercase, k=6))
        print(f"Confirmation code: {confirmation_code}")
        return confirmation_code

    print("Starting MCP server...")
    await mcp.run_streamable_http_async()


if __name__ == "__main__":
    asyncio.run(main())
