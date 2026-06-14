# Note Summarizer MCP

**Overview**

Note Summarizer MCP is a small project that collects, organizes, and summarizes notes written in Markdown. It includes a simple agent and an MCP-style server for processing and serving summaries of notes stored under the `md_files/` folder.

**Quick Start**

- **Setup:** Install dependencies from `requirements.txt`.

```bash
pip install -r requirements.txt
```

- **Run the MCP server:**

```bash
python mcp_server.py
```

- **Run the agent:**

```bash
python agent.py
```

**Files**

- **`agent.py`**: Agent entrypoint that interacts with the MCP server or runs local summarization flows.
- **`mcp_server.py`**: Minimal server for handling requests and coordinating summarization tasks.
- **`requirements.txt`**: Python dependencies.
- **`md_files/`**: Sample Markdown notes used as input (contains `ai.md`, `ml.md`, `neural_networks.md`, `python.md`).

**Usage**

- Place or edit Markdown notes in the `md_files/` folder.
- Start the server with `python mcp_server.py` and run `python agent.py` to trigger summarization flows.
- Summaries are printed to the console by default; extend the agent or server to save results to files or a database.

**Versions / Changelog**

This project tracks a small set of logical versions. Update these entries as you make changes.

- **v0.1.0 — Initial skeleton** (initial commit)
	- Project skeleton and basic README created.
	- Added `requirements.txt` and `md_files/` with sample notes.
- **v0.2.0 — Agent and server**
	- Added `agent.py` and `mcp_server.py` to provide a runnable agent and a server entrypoint.
- **v0.3.0 — Content and docs**
	- Added sample Markdown notes under `md_files/` and improved README with quick-start and usage instructions.

If you'd like a different versioning style (semantic tags, Git tags, or a CHANGELOG.md), I can add that.

**Contributing**

- Fork the repo, make changes in a branch, and open a pull request describing your changes.
- Keep dependency changes minimal and add tests if you add new behavior.

**License & Contact**

- Add a `LICENSE` file to declare project licensing. For questions, open an issue or contact the maintainer.
