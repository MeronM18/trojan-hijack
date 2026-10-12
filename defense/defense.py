"""Defense class: ties the three layers together.

Will expose the interface Jazz's agent calls:
  protect_content(raw_text, source) -> str       (Layer 1 then Layer 2, if enabled)
  guard_action(name, args)          -> Decision  (Layer 3, if enabled)
  system_prompt_addendum()          -> str       (empty if Layer 2 is off)
  events                            -> list of what each layer did (used by eval)
  tainted                           -> True once Layer 1 flags anything
With every layer off it passes everything through unchanged (the baseline).
"""
