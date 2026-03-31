from __future__ import annotations

from acyresys.model import Event, EventKind, Severity


def strix_credential_theft(asset_id: str, step: int = 1) -> Event:
    return Event(
        step=step,
        asset_id=asset_id,
        kind=EventKind.ATTACK,
        summary="Strix simulates credential theft attempt",
        severity=Severity.HIGH,
        data={
            "actor": "strix",
            "attack_type": "credential_theft",
            "ttp": "credential-access",
            "bounded": True,
        },
    )


def strix_lateral_movement(asset_id: str, step: int = 1) -> Event:
    return Event(
        step=step,
        asset_id=asset_id,
        kind=EventKind.ATTACK,
        summary="Strix simulates bounded lateral movement",
        severity=Severity.CRITICAL,
        data={
            "actor": "strix",
            "attack_type": "lateral_movement",
            "ttp": "lateral-movement",
            "bounded": True,
        },
    )


def config_drift(asset_id: str, step: int = 1) -> Event:
    return Event(
        step=step,
        asset_id=asset_id,
        kind=EventKind.TELEMETRY,
        summary="Observed configuration drift",
        severity=Severity.MEDIUM,
        data={"drift": True, "source": "telemetry-agent"},
    )


def strix_destructive_wiper(asset_id: str, step: int = 1) -> Event:
    return Event(
        step=step,
        asset_id=asset_id,
        kind=EventKind.ATTACK,
        summary="Strix simulates destructive wiper behavior",
        severity=Severity.CRITICAL,
        data={
            "actor": "strix",
            "attack_type": "destructive_wiper",
            "ttp": "impact",
            "bounded": True,
        },
    )


SCENARIOS = {
    "credential-theft": strix_credential_theft,
    "lateral-movement": strix_lateral_movement,
    "config-drift": config_drift,
    "destructive-wiper": strix_destructive_wiper,
}
