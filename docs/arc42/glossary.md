# Glossar

Dieses Glossar erklärt die im Repository verwendeten Fachbegriffe so, dass sie im Projektkontext eindeutig lesbar bleiben.

## ACyReSys

Abkürzung für `Autonomous Cyber Resilience System`.
Im aktuellen Repo ist damit eine Architekturhypothese und ein Prototyp gemeint, kein fertiges Produkt.

## Adversarial

Bezeichnet einen gegnerischen oder absichtlich herausfordernden Blick auf ein System.
Im Projekt meint es kontrollierte, feindliche Simulationen zur Prüfung der Resilienz.

## Append-only Journal

Ein Journal, das Einträge nur anhängt und nicht nachträglich überschreibt.
Es dient dazu, Entscheidungen und Zustandswechsel nachvollziehbar zu machen.

## Architekturhypothese

Eine begründete Annahme darüber, wie ein System sinnvoll aufgebaut sein könnte.
Sie ist ein Entwurf und muss durch Prototypen, Tests oder Betriebserfahrung validiert werden.

## Asset

Ein schützenswertes Objekt im System.
Im Prototyp ist das zum Beispiel ein Dienst oder eine Workload.

## Attack Surface

Die Summe der technisch angreifbaren Stellen eines Systems.
Dazu gehören etwa Netzwerkschnittstellen, Konfigurationen, Identitäten oder Laufzeitkomponenten.

## Bounded Automation

Automatisierung mit klaren Grenzen.
Das System darf nur innerhalb definierter Sicherheits- und Wirkungslimits autonom handeln.

## Blast Radius

Der Bereich, der von einem Fehler, Angriff oder Ausfall betroffen ist.
Der Begriff hilft dabei, die Auswirkungen einer Kompromittierung abzuschätzen.

## CLI

Abkürzung für `Command Line Interface`.
Das ist eine textbasierte Schnittstelle, über die der Prototyp lokal gestartet wird.

## Compromised

Ein Zustand, in dem ein Asset als nicht mehr vertrauenswürdig oder bereits verletzt gilt.
Dieser Zustand erfordert in der Regel starke Eindämmung oder menschliche Bewertung.

## Containment

Gezielte Eingrenzung eines Problems, damit es sich nicht weiter ausbreitet.
Das kann zum Beispiel Quarantäne oder das Sperren von Netzwerkverkehr sein.

## Control Loop

Ein wiederholter Zyklus aus Beobachtung, Bewertung, Entscheidung und Handlung.
Im Projekt ist das der Kernmechanismus von ACyReSys.

## Control Plane

Die logische Steuerungsebene eines Systems.
Sie trifft Entscheidungen, verwaltet Regeln und koordiniert Reaktionen.
Im Prototyp ist sie noch nicht als eigene technische Schicht getrennt umgesetzt.

## Credential Access

Versuch, an Anmeldedaten, Schlüssel oder andere Authentifizierungsinformationen zu gelangen.
Im Prototyp ist das ein simuliertes Angriffsszenario.

## Decision Engine

Komponente, die aus beobachteten Ereignissen eine Entscheidung ableitet.
Im Prototyp ist diese Logik in der Engine enthalten.

## Defense Layer

Der Teil des Systems, der auf erkannte Risiken reagiert.
Er umfasst im Prototyp vor allem die Reaktionslogik und die Response Tiers.

## Desired State

Der gewünschte oder erlaubte Zielzustand eines Assets oder Systems.
Er wird mit dem beobachteten Zustand verglichen, um Abweichungen zu erkennen.

## Detection

Erkennung von Auffälligkeiten, Angriffen, Regelverletzungen oder Drift.
Erkennung allein reicht nicht aus, ist aber der notwendige erste Schritt.

## Drift

Abweichung zwischen dem gewünschten und dem tatsächlich beobachteten Zustand.
Das kann durch Fehlkonfiguration, manuelle Änderungen oder unerwartetes Verhalten entstehen.

## Event

Ein einzelnes beobachtetes oder simuliertes Ereignis.
Im Prototyp wird daraus eine Entscheidung und später ein Journal-Eintrag abgeleitet.

## Governance

Rahmen aus Regeln, Verantwortlichkeiten und Grenzen, der autonomes Verhalten kontrolliert.
Im Projekt ist Governance besonders wichtig, um übergriffige oder gefährliche Automation zu vermeiden.

## Healing

Kurzform für Wiederherstellung oder Reparatur eines betroffenen Zustands.
Im Projekt meint das nicht nur Neustart, sondern eine gezielte Rückführung in einen akzeptablen Zustand.

## Human Gate

Stelle im Ablauf, an der ein Mensch eine riskante Aktion freigeben oder stoppen muss.
Das ist ein Schutzmechanismus gegen überzogene Autonomie.

## Ist-Zustand

Der tatsächlich beobachtete Zustand eines Systems oder Assets.
Im Englischen meist `Observed State`.

## Journalisierung

Das strukturierte Festhalten von Ereignissen, Entscheidungen und Ergebnissen.
Sie ist wichtig für Nachvollziehbarkeit, Revision und spätere Analyse.

## Lateral Movement

Bewegung eines Angreifers innerhalb eines Systems von einem kompromittierten Teil zu weiteren Zielen.
Im Prototyp wird dieses Verhalten kontrolliert simuliert.

## Observed State

Der tatsächlich gemessene Zustand eines Assets oder Systems.
Er kann vom `Desired State` abweichen.

## Orchestrierung

Koordination mehrerer Schritte oder Komponenten in einer definierten Reihenfolge.
Später wäre das relevant für Recovery- und Response-Ketten.

## Policy

Eine explizite Regel, die festlegt, was erlaubt, verboten oder verpflichtend ist.
Policies steuern in solchen Systemen typischerweise Entscheidungen und Aktionen.

## Quarantäne

Isolation eines betroffenen Systems oder Teilsystems.
Ziel ist es, weitere Ausbreitung zu verhindern und Zeit für Prüfung oder Recovery zu gewinnen.

## Recovery

Geplanter Wiederherstellungsprozess nach einer Störung oder einem Angriff.
Im Projekt ist Recovery nur dann sinnvoll, wenn danach auch verifiziert wird.

## Reconciliation

Rückführung eines Systems in den gewünschten Zustand.
Der Begriff ist aus deklarativen Infrastruktursystemen bekannt.

## Revalidation

Erneute Prüfung, ob ein Asset nach einer Maßnahme wieder als ausreichend vertrauenswürdig gelten kann.
Im Prototyp ist das ein eigener Zustand vor der finalen Rückkehr zu `healthy`.

## Resilienz

Fähigkeit eines Systems, Störungen oder Angriffe zu verkraften, sich anzupassen und weiter funktionsfähig zu bleiben.
Resilienz ist mehr als reine Abwehr.

## Response Tier

Eine Stufe, die festlegt, wie weit das System autonom reagieren darf.
Im Prototyp gibt es vier Stufen von Beobachtung bis menschlicher Freigabe.

## Self-Healing

Fähigkeit eines Systems, sich teilweise selbst in einen besseren Zustand zurückzuführen.
Das schließt im Projekt auch Revalidation und Erfolgsprüfung ein.

## Simulator

Eine kontrollierte Umgebung oder Logik, die Verhalten nachstellt.
`Strix` ist im Projekt ein Simulator für adversariale Situationen, kein frei agierender Angreifer.

## Soll-Zustand

Deutsche Beschreibung für `Desired State`.
Er beschreibt den angestrebten oder erlaubten Zustand.

## Strix

Der Name des kontrollierten adversarialen Simulators im Projekt.
Strix soll ACyReSys prüfen, nicht unkontrolliert angreifen.

## Threat Model

Beschreibung möglicher Bedrohungen, Angreiferfähigkeiten und relevanter Risiken.
Ein gutes Threat Model hilft, sinnvolle Detection- und Recovery-Mechanismen abzuleiten.

## Trust Score

Ein numerischer Ausdruck dafür, wie vertrauenswürdig ein Asset aktuell eingeschätzt wird.
Im Prototyp ist das ein einfaches Hilfsmittel für Zustandsübergänge.

## Verification

Prüfung, ob eine ausgeführte Maßnahme tatsächlich zum gewünschten Ergebnis geführt hat.
Ohne Verification bleibt Recovery nur eine Behauptung.

## Workload

Eine ausführbare Einheit wie ein Dienst, Container oder Prozess.
Im Projekt kann eine Workload Ziel von Isolation, Recovery oder Bewertung sein.
