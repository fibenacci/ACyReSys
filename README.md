# ACyReSys

`ACyReSys` steht für `Autonomous Cyber Resilience System`.

> [!IMPORTANT]
> Dieses Repository ist derzeit eine Architekturhypothese und ein Experiment zur Validierung der zugrunde liegenden Idee hinter ACyReSys.
> Es beschreibt noch kein fertiges Produkt und keinen produktionsreifen Sicherheitsansatz, sondern einen bewusst eingegrenzten Prototypen zur technischen und konzeptionellen Exploration.

Das Ziel ist kein weiterer statischer Security-Stack, sondern ein kontrolliertes Resilienzsystem, das Angriffe simuliert, Risiken bewertet, begrenzt autonom reagiert und Wiederherstellung nachvollziehbar verifiziert.

Der aktuelle Stand ist bewusst ein früher Prototyp: lokal, deterministisch, klein im Scope und auf Architekturvalidierung ausgelegt.

## Leitidee

ACyReSys folgt einem geschlossenen, aber begrenzten Sicherheitszyklus:

`Observe -> Detect -> Decide -> Act -> Recover -> Verify`

Die zentrale Annahme dabei ist:
Sicherheit entsteht nicht nur durch Erkennung, sondern durch die Fähigkeit, einen nachweisbar besseren Zustand wiederherzustellen.

## Was der Prototyp heute abbildet

- `Strix` als kontrollierten feindseligen Simulator
- einen Defense-Layer mit expliziten Reaktionsstufen
- einen Self-Healing- und Revalidation-Workflow
- ein append-only Journal für Entscheidungen und Zustandswechsel
- ein kleines CLI für reproduzierbare lokale Szenarien

## Architektur

### Kernbausteine

- `acyresys/model.py`
  Formales Domänenmodell für Assets, Events, Decisions und Journal-Einträge.
- `acyresys/engine.py`
  Deterministischer Control Loop mit Zustandsautomat, Entscheidungslogik, Recovery und Verification.
- `acyresys/scenarios.py`
  Bounded `Strix`-Szenarien und Telemetrie-Inputs für die Simulation.
- `acyresys/cli.py`
  Schmale CLI zum Ausführen und Inspizieren einzelner Szenarien.

### Zustandsmodell

Ein Asset bewegt sich im Prototyp durch diese Sicherheitszustände:

- `healthy`
- `degraded`
- `suspicious`
- `quarantined`
- `recovering`
- `revalidated`
- `compromised`

Wichtig ist die Trennung zwischen `Desired State` und `Observed State`.
ACyReSys soll nicht nur Alarm erzeugen, sondern die Abweichung vom Soll-Zustand sichtbar und behandelbar machen.

### Response Tiers

Autonomie ist im Prototyp absichtlich begrenzt:

- `OBSERVE_ONLY`
  Nur beobachten, korrelieren und Telemetrie anreichern.
- `SAFE_AUTONOMOUS`
  Niedrigriskante Aktionen wie Secret Rotation oder Config Reconciliation.
- `CONTROLLED_CONTAINMENT`
  Harte, aber begrenzte Eingriffe wie Quarantäne oder Containment.
- `HUMAN_GATED`
  Aktionen außerhalb des autonomen Sicherheitsbudgets.

Damit bleibt ACyReSys ein kontrollierbares System und kein ungebremster Sicherheitsautomat.

## Warum dieser Ansatz relevant ist

Viele bestehende Security-Systeme enden bei `Detect -> Alert -> Ticket`.
ACyReSys setzt früher an und denkt Security als zustandsbasiertes Resilienzsystem:

- nicht nur `Known Bad`, sondern auch Drift und Vertrauensverlust
- nicht nur Reaktion, sondern Wiederherstellung
- nicht nur Automation, sondern bounded automation
- nicht nur Ereignisse, sondern rekonstruierbare Entscheidungen

## Schnellstart

Voraussetzung: `Python 3.12+`

Beispiele:

```bash
python3 -m acyresys.cli --scenario credential-theft
python3 -m acyresys.cli --scenario lateral-movement
python3 -m acyresys.cli --scenario destructive-wiper --json
python3 -m acyresys.cli --scenario config-drift --json
```

## Szenarien

- `credential-theft`
  Kontrollierte Credential-Access-Simulation durch `Strix`, gefolgt von Secret Rotation und Revalidation.
- `lateral-movement`
  Bounded Lateral-Movement-Simulation mit Containment und anschließender Verifikation.
- `destructive-wiper`
  Bewusst nicht-autonomer Impact-Fall, der in `HUMAN_GATED` endet.
- `config-drift`
  Nicht-adversarialer Drift-Fall für Reconciliation und Healing.

## Repository-Struktur

```text
.
├── docs/
│   └── arc42/
│       ├── glossary.md
│       └── README.md
├── README.md
├── pyproject.toml
└── acyresys/
    ├── __init__.py
    ├── cli.py
    ├── engine.py
    ├── model.py
    └── scenarios.py
```

## Bewusste Grenzen

Dieser Prototyp hat absichtlich noch keine:

- echten Sensoren oder Runtime-Integrationen
- persistente Datenhaltung
- Policy-DSL oder Governance-Engine
- Lern-, Update- oder RL-Layer
- Multi-Asset-Dependency-Graph-Auswertung
- produktionssichere Isolation, Rotation oder Patch-Orchestrierung

Er validiert die Domäne, nicht den kompletten Plattformbau.

## Nächste sinnvolle Schritte

Wenn wir daraus ein belastbares System entwickeln wollen, sind die nächsten sauberen Schritte:

1. persistentes Event- und Decision-Journal mit Replay
2. Policy-Modell für erlaubte autonome Aktionen und Budgets
3. Multi-Asset-Graph für Blast-Radius und Dependencies
4. getrennte Simulation Plane für `Strix`
5. echte Healing-Runner für Container- oder Service-Umgebungen

## Arbeitsregeln

Die Repo-spezifischen Agenten- und Architekturregeln stehen in `AGENTS.md`.

## Dokumentation

- `docs/arc42/README.md`
  Erste arc42-Dokumentation der aktuellen Architekturhypothese.
- `docs/arc42/glossary.md`
  Glossar für Fachbegriffe und Projektsprache.
