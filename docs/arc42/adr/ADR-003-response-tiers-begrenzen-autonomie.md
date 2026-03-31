# ADR-003: Response Tiers begrenzen Autonomie

## Status

Akzeptiert

## Kontext

Autonome Sicherheitssysteme können selbst Schaden verursachen, wenn Eingriffe unklar oder zu weitreichend sind.

## Entscheidung

ACyReSys verwendet explizite Response Tiers für autonome Maßnahmen.

## Begründung

- kontrollierbare Wirkung
- bessere Governance
- klare Trennung zwischen Beobachtung, sicherer Automation und menschlicher Freigabe

## Konsequenzen

- mehr Modellierungsaufwand
- Entscheidungen müssen erklärt und klassifiziert werden
- riskante Aktionen bleiben human-gated
