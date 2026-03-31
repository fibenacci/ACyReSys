# ADR-001: Deterministischer Einzelprozess-Prototyp

## Status

Akzeptiert

## Kontext

ACyReSys ist derzeit eine Architekturhypothese.
Der Kern muss zunächst fachlich validiert werden, bevor verteilte Infrastruktur oder komplexe Integrationen sinnvoll sind.

## Entscheidung

Der erste Prototyp bleibt ein lokaler Python-Prozess mit deterministischem Verhalten.

## Begründung

- einfache Nachvollziehbarkeit
- geringe technische Ablenkung
- leichter testbar
- schnelle Iteration auf dem Domänenmodell

## Konsequenzen

- keine echte Verteilung
- keine Persistenz oder externe Backends
- Fokus auf Modell, Entscheidungslogik und Dokumentation
