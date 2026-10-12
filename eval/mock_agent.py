"""Minimal stand-in agent so the eval runs before Jazz's agent exists.

Will be a small Claude tool-use loop (Haiku by default) with the same
load_content(source) / run_tool(name, args) contract and fake tools
(read_file, send_email, share_file, read_webpage) that log to a per-run file.
"""
