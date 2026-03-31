"""Multi‑agent workflow demonstration.

Defines simple planner, executor and reviewer agents.  These agents
are intentionally simplistic and do not call external APIs.  They
illustrate how tasks can be decomposed and processed in stages.
"""

from __future__ import annotations

from typing import List


class Planner:
    """A trivial planner that creates one subtask from a request."""

    def plan(self, request: str) -> List[str]:
        # In a real system this might involve parsing the request and
        # generating multiple subtasks; here we return the original request.
        return [request]


class Executor:
    """A simple executor that interprets arithmetic expressions."""

    def execute(self, action: str) -> str:
        # WARNING: Using eval on arbitrary input can be dangerous.  This is safe
        # here because we control the input.  Do not use eval on untrusted data.
        try:
            result = eval(action, {"__builtins__": {}}, {})
            return str(result)
        except Exception as exc:
            return f"Error: {exc}"


class Reviewer:
    """A reviewer that checks whether the result is an integer."""

    def review(self, request: str, result: str) -> bool:
        # In a real system this might verify correctness against an expected answer.
        # Here we simply check that the result is a string representation of an integer.
        try:
            int(result)
            return True
        except ValueError:
            return False


def run_workflow(request: str) -> str:
    """Run the planner, executor and reviewer on a request.

    Returns a message describing whether the task succeeded.
    """
    planner = Planner()
    executor = Executor()
    reviewer = Reviewer()

    plan = planner.plan(request)
    if not plan:
        return "Planner returned no actions."
    # For this demo we assume a single action
    action = plan[0]
    result = executor.execute(action)
    approved = reviewer.review(request, result)
    if approved:
        return f"Task: {request}\nResult: {result}\nStatus: Approved"
    else:
        return f"Task: {request}\nResult: {result}\nStatus: Rejected"


__all__ = ["Planner", "Executor", "Reviewer", "run_workflow"]