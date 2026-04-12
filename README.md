# AI Agent

A small CLI coding agent built on the Google GenAI Python SDK. The agent accepts a natural-language prompt, can call a limited set of local tools, feeds tool results back into the model, and stops when the model returns a normal text answer.

Current tool support:

- List files in a directory
- Read text files
- Run Python files with optional arguments
- Write or overwrite files

The agent is currently wired to operate inside the sample [calculator](./calculator) workspace when it makes tool calls.

## How It Works

The entry point is [main.py](./main.py).

1. The script loads `GEMINI_API_KEY` from the environment.
2. It sends the user prompt and tool schemas to Gemini.
3. If the model returns a function call, the app dispatches that call through [functions/call_function.py](./functions/call_function.py).
4. The tool result is wrapped as a function response and appended back into the conversation.
5. The loop repeats for up to 20 iterations, or stops earlier when the model returns plain text.

This gives the project a simple tool-use feedback loop rather than a single-shot completion flow.

## Project Layout

- [main.py](./main.py): CLI entry point and feedback loop
- [prompts.py](./prompts.py): model name and system instruction
- [config.py](./config.py): shared configuration such as maximum file read size
- [functions/](./functions): tool implementations and tool schema declarations
- [calculator/](./calculator): sample working directory the agent currently operates on
- [_testing/](./_testing): simple scripts for manually exercising individual tools

## Available Tools

### `get_files_info`

Lists files in a directory relative to the working directory and returns each entry's name, size, and directory status.

### `get_file_content`

Reads a text file relative to the working directory. Output is truncated after `MAX_CHARS`, which is currently set to `10000`.

### `run_python_file`

Runs a `.py` file relative to the working directory with optional CLI arguments and returns captured stdout and stderr.

### `write_file`

Writes text to a file relative to the working directory, creating parent directories if needed.

## Security Model

Each file-oriented function validates paths with [functions/verify_file_path.py](./functions/verify_file_path.py) and rejects attempts to escape the permitted working directory.

In the current implementation, [functions/call_function.py](./functions/call_function.py) injects `./calculator` as the working directory for tool execution. That means the agent can only read, write, list, or run files inside the calculator example tree.

## Requirements

- Python 3.13+
- A valid `GEMINI_API_KEY`
- These Python packages:
	- `google-genai==1.12.1`
	- `python-dotenv==1.1.0`

## Setup

Create and activate a virtual environment, then install the dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install google-genai==1.12.1 python-dotenv==1.1.0
```

Create a `.env` file in the repository root:

```env
GEMINI_API_KEY=your_api_key_here
```

## Usage

Run the agent from the repository root:

```bash
python main.py "list the files in the current directory"
```

Verbose mode shows token counts and tool responses:

```bash
python main.py "read the calculator main file" --verbose
```

Example prompts:

```bash
python main.py "show me the files in the current directory"
python main.py "read pkg/calculator.py"
python main.py "run main.py with the argument 3 + 5"
python main.py "write a notes.txt file with hello world"
```

Because tool calls are scoped to `./calculator`, paths in prompts should be relative to that directory.

## Calculator Sample App

The included [calculator](./calculator) directory is a small infix-expression calculator used as the agent's active working area.

Highlights:

- Supports `+`, `-`, `*`, `/`, and parentheses
- Returns JSON output from [calculator/pkg/render.py](./calculator/pkg/render.py)
- Includes unit tests in [calculator/tests.py](./calculator/tests.py)

Example:

```bash
python calculator/main.py "3 * (4 + 5)"
```

## Current Limitations

- The working directory for tool calls is hardcoded to `./calculator`.
- The main loop executes at most 20 tool/model iterations.
- The tool set is intentionally small and limited to local file and Python execution tasks.
- The README reflects the code as it exists now, including those constraints.

## Development Notes

The project includes small manual test scripts in [_testing](./_testing) for exercising individual functions directly. These are useful for quick local checks while iterating on the tool layer.
