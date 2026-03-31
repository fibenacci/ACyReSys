from __future__ import annotations

from dataclasses import asdict

from acyresys.model import (
    Asset,
    AssetState,
    Decision,
    Event,
    EventKind,
    JournalEntry,
    ResponseTier,
    Severity,
)


class ACyReSysEngine:
    """Small deterministic prototype of the ACyReSys control loop."""

    def __init__(self) -> None:
        self.assets: dict[str, Asset] = {}
        self.journal: list[JournalEntry] = []
        self.step = 0

    def register_asset(self, asset: Asset) -> None:
        self.assets[asset.asset_id] = asset
        self._record(asset.asset_id, "register", "asset registered", asdict(asset))

    def ingest(self, event: Event) -> None:
        self.step = max(self.step, event.step)
        self._record(event.asset_id, event.kind.value, event.summary, event.data)

    def analyze(self, event: Event) -> Decision:
        asset = self.assets[event.asset_id]
        tier = ResponseTier.OBSERVE_ONLY
        action = "monitor"
        confidence = 0.45
        reason = "No strong indicator yet."
        requires_human = False

        if event.kind == EventKind.ATTACK:
            attack_type = event.data.get("attack_type")
            if attack_type == "credential_theft":
                asset.observed_state = AssetState.SUSPICIOUS
                asset.trust_score -= 35
                tier = ResponseTier.SAFE_AUTONOMOUS
                action = "rotate_secrets"
                confidence = 0.78
                reason = "Suspicious credential access pattern detected."
            elif attack_type == "lateral_movement":
                asset.observed_state = AssetState.QUARANTINED
                asset.trust_score -= 55
                tier = ResponseTier.CONTROLLED_CONTAINMENT
                action = "quarantine_workload"
                confidence = 0.9
                reason = "High-confidence lateral movement requires containment."
            elif attack_type == "destructive_wiper":
                asset.observed_state = AssetState.COMPROMISED
                asset.trust_score -= 80
                tier = ResponseTier.HUMAN_GATED
                action = "fail_closed_and_page_operator"
                confidence = 0.96
                reason = "Potentially destructive action exceeds autonomous budget."
                requires_human = True

        elif event.kind == EventKind.TELEMETRY and event.data.get("drift"):
            asset.observed_state = AssetState.DEGRADED
            asset.trust_score -= 15
            tier = ResponseTier.SAFE_AUTONOMOUS
            action = "reconcile_config"
            confidence = 0.7
            reason = "Observed drift from desired state can be safely reconciled."

        decision = Decision(
            step=event.step,
            asset_id=event.asset_id,
            response_tier=tier,
            action=action,
            reason=reason,
            requires_human=requires_human,
            confidence=confidence,
            data={"event_kind": event.kind.value, "severity": event.severity.value},
        )
        self._record(
            event.asset_id,
            "decision",
            f"tier={tier.name.lower()} action={action}",
            asdict(decision),
        )
        return decision

    def act(self, decision: Decision) -> str:
        asset = self.assets[decision.asset_id]
        outcome = "no-op"

        if decision.action == "monitor":
            outcome = "telemetry_enhanced"
        elif decision.action == "reconcile_config":
            asset.observed_state = AssetState.RECOVERING
            outcome = "config_reconciliation_started"
        elif decision.action == "rotate_secrets":
            asset.observed_state = AssetState.RECOVERING
            asset.notes.append("credentials rotated")
            outcome = "secrets_rotated"
        elif decision.action == "quarantine_workload":
            asset.observed_state = AssetState.QUARANTINED
            asset.notes.append("network egress blocked")
            outcome = "workload_quarantined"
        elif decision.action == "fail_closed_and_page_operator":
            asset.notes.append("operator review required")
            outcome = "awaiting_human_approval"

        self._record(
            decision.asset_id,
            "action",
            outcome,
            {"action": decision.action, "requires_human": decision.requires_human},
        )
        return outcome

    def recover(self, asset_id: str) -> str:
        asset = self.assets[asset_id]
        if asset.observed_state in {AssetState.RECOVERING, AssetState.QUARANTINED}:
            asset.observed_state = AssetState.REVALIDATED
            asset.trust_score = min(asset.trust_score + 25, 100)
            message = "asset revalidated after bounded recovery workflow"
        elif asset.observed_state == AssetState.DEGRADED:
            asset.observed_state = AssetState.HEALTHY
            asset.trust_score = min(asset.trust_score + 10, 100)
            message = "drift repaired"
        else:
            message = "no recovery required"

        self._record(asset_id, "recovery", message, asdict(asset))
        return message

    def verify(self, asset_id: str) -> bool:
        asset = self.assets[asset_id]
        success = (
            asset.observed_state in {AssetState.HEALTHY, AssetState.REVALIDATED}
            and asset.trust_score >= 60
        )
        message = "verification_passed" if success else "verification_failed"
        self._record(asset_id, "verification", message, asdict(asset))

        if success and asset.observed_state == AssetState.REVALIDATED:
            asset.observed_state = AssetState.HEALTHY

        return success

    def snapshot(self) -> dict[str, dict[str, object]]:
        return {
            asset_id: {
                "desired_state": asset.desired_state.value,
                "observed_state": asset.observed_state.value,
                "trust_score": asset.trust_score,
                "notes": list(asset.notes),
            }
            for asset_id, asset in self.assets.items()
        }

    def _record(
        self, asset_id: str, stage: str, message: str, payload: dict[str, object]
    ) -> None:
        self.journal.append(
            JournalEntry(
                step=self.step,
                asset_id=asset_id,
                stage=stage,
                message=message,
                payload=payload,
            )
        )
