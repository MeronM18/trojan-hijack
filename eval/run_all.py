"""Main evaluation entry point.

Will run every attack (and benign case) under each defense config, N trials each,
and write one row per run to eval/results/results_<model>.csv: case id, kind,
config, model, trial, L1 flagged, attack attempted, attack executed, stopped by
which layer, benign task ok.
Planned flags: --attacks, --benign, --configs, --trials, --model, --agent mock|jazz,
--approver, --dry-run (stretch, uses obedient_agent.py).
"""
