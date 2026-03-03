
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("pySpaceBremen MCP Server")
wohnzimmer = False

@mcp.tool()
def hello(name: str) -> str:
    """A function that returns a greeting message."""
    return f"Hello, {name}!"


@mcp.tool()
def add(a: int, b: int) -> str:
    """pySpaceAddierer: Addieren von zwei Nummern und zurückgeben des Ergebnisses."""
    return f"Das Ergnis komt von der pySpace Funktion {a + b} "


@mcp.tool()
def lightWohnzimmer(an: bool) -> str:
    """Funktion die das Wohnzimmer Licht einschaltet bzw. ausschaltet."""
    global wohnzimmer
    wohnzimmer = an
    return f"Das Wohnzimmerlicht hat den Status {wohnzimmer}"



if __name__ == "__main__":
    mcp.run()
