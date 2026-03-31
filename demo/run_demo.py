#!/usr/bin/env python3
"""Run the multi‑agent workflow demo.

Executes a simple arithmetic request through the planner, executor
and reviewer agents and prints the outcome.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.agent_workflow import run_workflow  # type: ignore


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Multi‑agent workflow demo")
    parser.add_argument("request", nargs="?", default="3 + 5", help="Arithmetic expression to evaluate")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    output = run_workflow(args.request)
    print(output)


if __name__ == "__main__":
    main()