from __future__ import annotations

import argparse
import json
from dataclasses import asdict

from acyresys.engine import ACyReSysEngine
from acyresys.model import Asset
from acyresys.scenarios import SCENARIOS


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run the minimal ACyReSys prototype.")
    parser.add_argument(
        "--scenario",
        choices=sorted(SCENARIOS),
        default="credential-theft",
        help="Simulation scenario to execute.",
    )
    parser.add_argument(
        "--asset-id",
        default="svc-payments",
        help="Identifier of the protected asset.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit machine-readable output.",
    )
    return parser


def main() -> None:
    args = build_parser().parse_args()

    engine = ACyReSysEngine()
    engine.register_asset(
        Asset(
            asset_id=args.asset_id,
            asset_type="service",
            capabilities=["restart", "quarantine", "rotate-secrets", "reconcile-config"],
        )
    )

    event = SCENARIOS[args.scenario](args.asset_id, step=1)
    engine.ingest(event)
    decision = engine.analyze(event)
    action_outcome = engine.act(decision)
    recovery_outcome = engine.recover(args.asset_id)
    verification = engine.verify(args.asset_id)

    result = {
        "scenario": args.scenario,
        "event": asdict(event),
        "decision": asdict(decision),
        "action_outcome": action_outcome,
        "recovery_outcome": recovery_outcome,
        "verification": verification,
        "assets": engine.snapshot(),
        "journal": [asdict(entry) for entry in engine.journal],
    }

    if args.json:
        print(json.dumps(result, indent=2))
        return

    print(f"ACyReSys scenario: {args.scenario}")
    print(f"asset: {args.asset_id}")
    print(
        "decision:"
        f" tier={decision.response_tier.name.lower()} action={decision.action}"
        f" confidence={decision.confidence:.2f}"
    )
    print(f"action outcome: {action_outcome}")
    print(f"recovery outcome: {recovery_outcome}")
    print(f"verification: {'passed' if verification else 'failed'}")
    print("final asset snapshot:")
    print(json.dumps(engine.snapshot(), indent=2))


if __name__ == "__main__":
    main()
