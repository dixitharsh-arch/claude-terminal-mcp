import os
import subprocess
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("terminal-server")

DEFAULT_WORKSPACE = os.path.expanduser("~/Desktop/mcp_server/workspace")


@mcp.tool()
def run_command(command: str) -> str:
    """
    Run a terminal command inside the workspace directory.

    Args:
        command: The shell command to run.

    Returns:
        The command output or an error message.
    """
    try:
        result = subprocess.run(
            command,
            shell=True,
            cwd=DEFAULT_WORKSPACE,
            capture_output=True,
            text=True,
            timeout=30
        )
        return result.stdout + result.stderr
    except Exception as e:
        return str(e)


if __name__ == "__main__":
    mcp.run(transport="stdio")
