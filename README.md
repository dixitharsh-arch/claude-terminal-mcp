# claude-terminal-mcp
A lightweight Python-based Model Context Protocol (MCP) server that enables Claude Desktop to execute terminal commands inside a controlled local workspace using natural language instructions.

This project demonstrates how to build and connect a custom MCP server so Claude can safely interact with your local system.

⸻

🚀 Problem It Solves

When working locally, developers usually need to:
	•	Remember terminal commands like mkdir, ls, touch, etc.
	•	Manually type them into the terminal
	•	Switch between their AI assistant and shell

This creates unnecessary friction for simple tasks.

This MCP server removes that friction by allowing Claude Desktop to:
	•	Understand plain English instructions
	•	Convert them into terminal commands
	•	Execute them safely inside a predefined workspace

⸻

⚙️ Features
	•	Run terminal commands directly from Claude Desktop
	•	Convert natural language → shell commands
	•	Restrict execution to a safe workspace directory
	•	Minimal, beginner-friendly implementation
	•	Serves as a template for building custom Claude tools

⸻

🧪 Example Usage

In Claude chat:

Create a folder named project
→ executes mkdir project

Show me what files exist here
→ executes ls

Create a file called notes.txt
→ executes touch notes.txt

Where am I right now?
→ executes pwd

All commands run inside the configured workspace directory.

⸻

🛠 Tech Stack
	•	Python
	•	FastMCP / MCP SDK
	•	uv (environment & runner)
	•	Claude Desktop
	•	Git & GitHub

⸻

📂 Project Structure

claude-terminal-mcp/

main.py — MCP server implementation
workspace/ — safe execution directory
pyproject.toml — project configuration
README.md
.gitignore

⸻

🔧 Installation

Clone the repository

git clone https://github.com/dixitharsh-arch/claude-terminal-mcp.git
cd claude-terminal-mcp

Install dependencies

pip install mcp

OR

uv pip install mcp

⸻

▶️ Run MCP Server

uv run mcp run main.py

The server will start and wait for Claude Desktop to connect.

⸻

🔗 Connect to Claude Desktop

Open:

~/Library/Application Support/Claude/claude_desktop_config.json

Add inside "mcpServers":

“terminal-server”: {
“command”: “/Users/YOUR_USERNAME/.local/bin/uv”,
“args”: [
“run”,
“–with”,
“mcp[cli]”,
“mcp”,
“run”,
“/FULL/PATH/TO/main.py”
]
}

Replace YOUR_USERNAME and FULL/PATH accordingly, then restart Claude Desktop.

⸻

🧠 How It Works
	1.	Claude receives a natural language instruction
	2.	Claude calls the MCP tool exposed by this server
	3.	The server executes the corresponding shell command
	4.	Output is returned back to Claude

Communication happens via stdio transport using MCP protocol.

⸻

🔒 Safety
	•	Commands execute only inside the configured workspace directory
	•	Prevents accidental modification of system files
	•	Workspace path can be adjusted in main.py

⸻

🎯 Purpose of This Project

This is my first MCP server project, created to:
	•	Learn how MCP integrates local tools with Claude Desktop
	•	Explore AI-powered local automation workflows
	•	Provide a simple reference/template for others building MCP tools

⸻

🚀 Future Improvements
	•	Command safety filtering
	•	File read/write helper tools
	•	Directory navigation support
	•	Streaming command output
	•	Logging and monitoring
	•	Packaging as installable Python module

⸻

📜 License

MIT License
