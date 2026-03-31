# ADR-004: Recovery braucht Verifikation

## Status

Akzeptiert

## Kontext

Eine ausgeführte Maßnahme ist noch kein Beweis dafür, dass das System wieder in einem akzeptablen Zustand ist.

## Entscheidung

Recovery wird erst nach erfolgreicher Verifikation als wirksam betrachtet.

## Begründung

- vermeidet falsche Sicherheit
- stärkt Nachvollziehbarkeit
- passt zum Resilienzziel statt bloßer Aktionsausführung

## Konsequenzen

- zusätzlicher Prüfpfad nötig
- Zustandsmodell braucht Revalidation
- Journalisierung wird wichtiger
