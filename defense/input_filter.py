"""Layer 1: input filter.

Will scan raw incoming content (before any HTML-to-text conversion) for
suspicious instructions using the rules in rules.py.
  normalize(text) -> text with NFKC applied, zero-width chars removed, lowercased
  scan(text)      -> list of findings (which rules matched and where)
  sanitize(text)  -> ScanResult(flagged, findings, clean_text): removes hidden HTML,
                     replaces high-severity lines with a [removed by input filter]
                     marker, and adds a warning line at the top.
"""
