from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class AssetState(str, Enum):
    HEALTHY = "healthy"
    DEGRADED = "degraded"
    SUSPICIOUS = "suspicious"
    QUARANTINED = "quarantined"
    RECOVERING = "recovering"
    REVALIDATED = "revalidated"
    COMPROMISED = "compromised"


class EventKind(str, Enum):
    TELEMETRY = "telemetry"
    ATTACK = "attack"
    DETECTION = "detection"
    DECISION = "decision"
    ACTION = "action"
    RECOVERY = "recovery"
    VERIFICATION = "verification"


class Severity(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class ResponseTier(int, Enum):
    OBSERVE_ONLY = 0
    SAFE_AUTONOMOUS = 1
    CONTROLLED_CONTAINMENT = 2
    HUMAN_GATED = 3


@dataclass(slots=True)
class Asset:
    asset_id: str
    asset_type: str
    desired_state: AssetState = AssetState.HEALTHY
    observed_state: AssetState = AssetState.HEALTHY
    trust_score: int = 100
    capabilities: list[str] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)


@dataclass(slots=True)
class Event:
    step: int
    asset_id: str
    kind: EventKind
    summary: str
    severity: Severity = Severity.LOW
    data: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class Decision:
    step: int
    asset_id: str
    response_tier: ResponseTier
    action: str
    reason: str
    requires_human: bool
    confidence: float
    data: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class JournalEntry:
    step: int
    asset_id: str
    stage: str
    message: str
    payload: dict[str, Any] = field(default_factory=dict)
