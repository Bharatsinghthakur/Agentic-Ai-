from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Math")

@mcp.tool()
def add(a:int,b:int) -> int:
    """Add two numbers

    Args:
        a (int): _description_
        b (int): _description_

    Returns:
        int: return a + b
    """
    return a+b

@mcp.tool()
def multiply(a:int,b:int) -> int:
    """Multiply two numbers """
    return a*b

if __name__ == "__main__":
    mcp.run(transport="stdio")
    
"""
# The transport="stdio" argument tells the server to:
# use standard input/output (stdin and stdout) to receive and respond to tool function calls

"""

