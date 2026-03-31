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

- Planner decomposes user requests into structured, executable steps
- Executor processes tasks with defined input/output contracts
- Reviewer validates outputs against expected results before approval
- Implements basic retry and validation patterns to simulate production agent control flows
- Demonstrates deterministic execution paths across multi-stage workflows  

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
