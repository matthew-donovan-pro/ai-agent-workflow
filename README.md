# Multi‑Agent Workflow System

This repository illustrates a simple multi‑agent workflow.  The demonstration uses plain Python functions to represent a planner, executor and reviewer agent.  In a real AI system, these agents would wrap calls to large language models or other reasoning engines.

## Components

- **Planner** – decomposes a task into one or more subtasks.
- **Executor** – performs a subtask and returns a result.
- **Reviewer** – checks the results and approves or rejects them.

## Example

The demo solves a basic arithmetic problem, showing how information flows between agents:

1. The planner receives the request "Compute 3 + 5" and generates a plan: `["Add 3 and 5"]`.
2. The executor performs the operation and returns `8`.
3. The reviewer checks that the result is correct.

Run the demo with:

```bash
python demo/run_demo.py
```

## IP Notes

This is purely a demonstration; the planner, executor and reviewer agents here do not call external services.  Production workflows would involve LLM calls, chain‑of‑thought prompting and error handling which are not shown.