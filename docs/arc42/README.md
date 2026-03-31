# arc42 für ACyReSys

Diese Dokumentation beschreibt die aktuelle Architekturhypothese von `ACyReSys` im Format von `arc42`.

> [!IMPORTANT]
> Diese Architektur ist derzeit ein konzeptioneller Arbeitsstand für einen Prototypen.
> Sie dokumentiert Annahmen, Grenzen und Entwurfsentscheidungen, nicht den Stand eines produktionsreifen Systems.

## 1. Einführung und Ziele

### Aufgabenstellung

`ACyReSys` untersucht, ob ein zustandsbasiertes, teilweise autonomes Cyber-Resilienzsystem sinnvoll modelliert werden kann.
Der Fokus liegt aktuell auf einem kleinen, deterministischen Kontrollkern.

### Qualitätsziele

- Nachvollziehbarkeit von Entscheidungen
- Begrenzte und erklärbare Autonomie
- Trennung von Soll-Zustand und Ist-Zustand
- Verifizierbare Wiederherstellung statt bloßem Aktionismus
- Erweiterbarkeit für spätere Policy-, Recovery- und Simulationslogik

### Stakeholder

- Projektinitiator
- Architektur- und Sicherheitsinteressierte
- spätere Entwickler des Prototyps

## 2. Randbedingungen

- Die aktuelle Implementierung ist ein lokaler Python-Prototyp.
- Das Repository beschreibt eine Architekturhypothese, kein fertiges Produkt.
- `Strix` ist als kontrollierter Simulator gedacht, nicht als unbeschränkter Offensiv-Agent.
- Hochriskante Maßnahmen sollen nicht autonom ausgeführt werden.

## 3. Kontextabgrenzung

### Fachlicher Kontext

ACyReSys verarbeitet simulierte oder beobachtete Sicherheitsereignisse, bewertet sie gegen ein Zustandsmodell und leitet daraus kontrollierte Reaktionen sowie Recovery-Schritte ab.

### Technischer Kontext

Der aktuelle Prototyp besteht aus:

- Domänenmodell
- Entscheidungs- und Recovery-Engine
- Szenariodefinitionen
- lokaler CLI

Externe Sensoren, Orchestratoren, Datenbanken oder Policy-Backends sind noch nicht angeschlossen.

## 4. Lösungsstrategie

Die Lösungsstrategie für den Prototypen ist bewusst konservativ:

- kleiner, deterministischer Kern statt verteilter Plattform
- formales Zustandsmodell statt loser Event-Sammlung
- bounded automation statt maximaler Autonomie
- Journalisierung statt Blackbox-Verhalten
- Simulation vor echter operativer Integration

## 5. Bausteinsicht

### Überblick

- `acyresys/model.py`
  Enthält die zentralen Typen für Assets, Events, Decisions und Journal-Einträge.
- `acyresys/engine.py`
  Enthält die Steuerlogik für Analyse, Entscheidung, Aktion, Recovery und Verifikation.
- `acyresys/scenarios.py`
  Enthält kontrollierte Eingaben für Simulation und Validierung.
- `acyresys/cli.py`
  Startet reproduzierbare lokale Szenarien.

## 6. Laufzeitsicht

Ein typischer Ablauf im Prototyp:

1. Ein Asset wird registriert.
2. Ein Szenario erzeugt ein Event.
3. Die Engine bewertet das Event.
4. Es wird eine Entscheidung mit Reaktionsstufe erzeugt.
5. Eine begrenzte Aktion wird ausgeführt oder bewusst nicht autonom freigegeben.
6. Recovery und Verifikation prüfen, ob ein akzeptabler Zustand erreicht wurde.
7. Alle Schritte werden journalisiert.

## 7. Verteilungssicht

Der aktuelle Stand ist nicht verteilt.
Alles läuft lokal innerhalb eines Python-Prozesses.

Die spätere Zielrichtung kann getrennte Kontroll-, Simulations- und Ausführungsebenen umfassen, ist aber noch nicht implementiert.

## 8. Querschnittliche Konzepte

- Zustandsmodell für Sicherheits- und Vertrauenslagen
- Entscheidungsjournal als nachvollziehbare Spur
- Response Tiers zur Begrenzung autonomer Maßnahmen
- Recovery mit anschließender Verifikation
- klare Trennung zwischen Architekturhypothese und verifiziertem Verhalten

## 9. Architekturentscheidungen

### Deterministischer Prototyp

Der Einstieg erfolgt bewusst ohne verteilte Infrastruktur und ohne lernende Modelle.
So lässt sich die Kernlogik zuerst fachlich validieren.

### Bounded Automation

Der Prototyp darf nicht in eine unkontrollierte autonome Reaktionsmaschine kippen.
Deshalb sind Reaktionsstufen und Human Gates zentral.

### Simulation zuerst

Adversariale Logik wird zunächst nur als kontrollierte Simulation modelliert.
Das reduziert Risiko und schärft die Anforderungen an Detection, Recovery und Governance.

## 10. Qualitätsanforderungen

- Entscheidungen müssen nachvollziehbar sein.
- Aktionen müssen begründet und begrenzt sein.
- Wiederherstellung muss überprüfbar sein.
- Begriffe und Annahmen müssen klar dokumentiert sein.
- Erweiterungen dürfen die Architekturhypothese nicht stillschweigend in Produktbehauptungen verwandeln.

## 11. Risiken und technische Schulden

- Die aktuelle Architektur ist nur für einen kleinen Prototypen validiert.
- Es gibt noch keine echten Integrationen in Infrastruktur oder Security-Tools.
- Das Zustandsmodell ist nützlich, aber noch nicht empirisch validiert.
- Governance, Persistenz und Multi-Asset-Korrelation fehlen noch.
- Viele Begriffe stammen aus Security- und Architekturkontexten und müssen sauber definiert werden.

## 12. Glossar

Das Glossar liegt in [glossary.md](/home/fibenacci/Dokumente/Projekte/ACyReSys/docs/arc42/glossary.md) und beschreibt die im Repository verwendeten Fachbegriffe klar und knapp.
