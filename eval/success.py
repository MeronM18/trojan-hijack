"""Decides the outcome of a run.

Will parse machine-checkable conditions (email_to=..., file_shared=...,
output_contains=...) and check them against the action log and final output to
decide whether an attack was attempted/executed or a benign task succeeded.
"""
