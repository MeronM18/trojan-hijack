"""Layer 3: action approval.

Will define RISKY_TOOLS = {"send_email", "share_file"} and
check_action(name, args, approver, tainted) -> Decision(allowed, reason, warnings).
Risky actions get a plain summary plus warnings (unknown recipient, sensitive file
name, session tainted by Layer 1) and must be approved by an approver function:
  cli_approver            - asks the real user y/N in the terminal
  simulated_user_approver - eval stand-in that approves only actions the task asked for
  always_yes_approver     - careless user (stretch goal)
"""
