"""Layer 1 rule table.

Will hold a plain list of rules (name, regex, severity, category, description)
used by input_filter.py: override phrases ("ignore previous instructions"),
fake role markers (SYSTEM:, [INST]), hidden HTML (display:none, white text,
comments), invisible Unicode characters, and exfiltration hints.
"""
