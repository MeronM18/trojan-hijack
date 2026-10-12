"""Adapter between the eval and an agent.

Will provide one function, run one task with a given Defense, that calls either
mock_agent.py now or Jazz's agent later, and returns the final text plus the list
of attempted/executed tool calls.
"""
