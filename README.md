# google-adk

A collection of small agents built while learning [Google's Agent Development Kit (ADK)](https://google.github.io/adk-docs/). Each folder is a self-contained agent that can be run with the ADK CLI or web UI.

## Agents

| Folder | What it demonstrates |
|---|---|
| `test_bot/` | Minimal starter agent, used to verify the ADK setup |
| `google_agent/` | Agent using Google Search as a built-in tool |
| `tavily_search_agent/` | Agent using Tavily for web search |
| `world_clock_agent/` | Agent with a custom function tool (time lookup by city) |
| `code_execution_agent/` | Agent that writes and runs code via code execution |
| `course_refund_agent/` | Agent with custom tools backed by a SQLite database (refund requests) |

## Requirements

- Python 3.10+ (developed on 3.14)
- A Google API key ([Google AI Studio](https://aistudio.google.com/apikey))
- A Tavily API key (only for `tavily_search_agent`)

## Setup

```bash
git clone https://github.com/Vighnesh1045/google-adk.git
cd google-adk

python -m venv .venv-1
source .venv-1/Scripts/activate      # Windows Git Bash
# source .venv-1/bin/activate        # macOS / Linux

python -m pip install google-adk
```

## Configuration

Each agent reads its keys from a `.env` file inside its own folder. These files are git-ignored, so create them yourself:

```
# <agent_folder>/.env
GOOGLE_API_KEY=your_key_here
TAVILY_API_KEY=your_key_here    # tavily_search_agent only
```

Never commit `.env` files.

## Run

From the repo root (the folder that contains the agent folders):

```bash
adk web          # browser UI, pick an agent from the dropdown
adk run google_agent    # terminal chat with one agent
```

## Course refund agent: database setup

The SQLite database is not committed. Create it with the sample data first:

```bash
python course_refund_agent/database_setup.py
```

The data in the setup script is dummy data for demonstration.

## Project structure

```
google-adk/
├── code_execution_agent/
├── course_refund_agent/
│   ├── agent.py
│   ├── tools.py
│   └── database_setup.py
├── google_agent/
├── tavily_search_agent/
├── test_bot/
└── world_clock_agent/
```

Each agent folder follows the ADK layout: `__init__.py` and `agent.py` exposing a `root_agent`.

## License

Add a license of your choice (MIT is a common default for learning projects).
