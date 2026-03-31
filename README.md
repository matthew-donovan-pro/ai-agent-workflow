# Multi-Agent Workflow System

**Multi-stage agent workflow demo using planner, executor, and reviewer roles for structured task processing.**

---

## Overview

This project demonstrates how complex tasks can be decomposed into coordinated agent stages to improve structure and reliability.

It shows:
- task decomposition into actionable steps  
- staged execution through defined roles  
- validation of outputs before final approval  

The implementation uses simple Python functions to make the workflow explicit. In production, these agents would interface with LLMs, external tools, and error-handling layers.

---

## Components

- **Planner** — decomposes a task into one or more subtasks  
- **Executor** — performs actions and produces results  
- **Reviewer** — validates outputs and determines acceptance  

---

## Example

The demo processes a simple task:

1. Planner receives: `"Compute 3 + 5"`  
2. Planner generates: `["Add 3 and 5"]`  
3. Executor returns: `8`  
4. Reviewer validates the result  

This illustrates how control flow moves through the system.

---

## Demo

Run:

```bash
python demo/run_demo.py
