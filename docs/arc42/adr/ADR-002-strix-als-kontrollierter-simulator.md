# ADR-002: Strix als kontrollierter Simulator

## Status

Akzeptiert

## Kontext

Der adversariale Teil von ACyReSys darf den Prototyp nicht in eine unkontrollierte offensive Plattform verwandeln.

## Entscheidung

`Strix` wird als kontrollierter adversarialer Simulator modelliert.

## Begründung

- geringeres Risiko
- klarere Anforderungen an Detection und Recovery
- bessere Trennung von Hypothese und operativer Realität

## Konsequenzen

- keine freie Exploit-Logik
- nur definierte Szenarien und Testpfade
- Governance bleibt zentral
