# Großen Kontext verstehen: klein anfangen und ehrlich prüfen

## 1. Ziel
Du prüfst, ob dein vorhandenes Modell drei Codes am Anfang, in der Mitte und am Ende eines selbst erzeugten Datenblocks richtig wiederfindet. Zunächst nur 50 neutrale Zeilen, nicht automatisch 220000 Tokens. Das ist Informationssuche in synthetischen Daten, keine Buchverständnis- oder Programmierabnahme.

## 2. Voraussetzungen und Download
Vorhandenes Python3, eigener bereits eingerichteter Modellserver und passender Client. Entpacke den vollständigen ZIP in einen neuen Lernordner. Das Paket enthält keinen Server, keine Modellgewichte und keinen automatischen HTTP-Aufruf. Lies KONTEXT-UEBUNG.py und QUELLEN.md.

## 3. Nur Quellen vorbereiten
Im entpackten Lernordner:

```powershell
python ./KONTEXT-UEBUNG.py prepare --output ./mein-kontexttest --lines 50
```

Ein vorhandener Zielordner wird erhalten. Der Helfer schreibt DATENBLOCK.txt, AUFTRAG.txt, ERWARTET.json und VORBEREITUNG.json. Letztere dokumentiert Bytes und Hash, ausdrücklich keine gemessene Tokenzahl. Python oder Modelle werden nicht installiert. 2 bis2000 neutrale Zeilen sind erlaubt; der Helfer baut keinen riesigen ungeprüften 220K-Aufruf.

## 4. Den Auftrag ansehen
AUFTRAG.txt enthält den vollständigen Datenblock und fordert exakt drei JSON-Felder. Die Codes sind eigene synthetische Zeichenketten. Bevor du sie sendest, kontrolliere Modell, Kontextgrenze, Werkzeugrechte und den tatsächlich verfügbaren Speicher. Andere laufende Aufträge nicht durch einen Modellwechsel unterbrechen.

## 5. Die echte Anfrage selbst auslösen
Benutze deinen schon funktionierenden Client aus unserem Vulkan-/Server-Tutorial. Füge den vollständigen AUFTRAG.txt-Inhalt ein, nicht ERWARTET.json. Bitte nur um die JSON-Antwort. Speichere tatsächlich zurückgegebenes JSON als ANTWORT.json im neuen Testordner. Erklärungstext oder Markdown-Codezäune sind hier kein schema-konformes JSON; bei Bedarf getrennt korrigieren lassen. Bei fehlender oder abgebrochener Antwort nichts als bestanden markieren.

## 6. Das Ergebnis exakt prüfen
```powershell
python ./KONTEXT-UEBUNG.py check --directory ./mein-kontexttest --result ./mein-kontexttest/ANTWORT.json
$LASTEXITCODE
```

Der Prüfer verlangt genau die drei Schlüssel und die zugehörigen Codes. Vertauschte Werte, zusätzliche Felder und bloße Code-Erwähnungen im Text reichen nicht. Ein bestandener eigener Prüfertest ist keine neue Modellantwort. Einen Hash kannst du zum Erhalten der echten Datei notieren.

## 7. Tokens, Bytes und Zeilen auseinanderhalten
Tokens sind modellabhängige Textstücke. Gleiche Bytes oder gleich viele Wörter garantieren keine gleiche Tokenzahl. Eine vorhandene llama.cpp-Tokenizerschnittstelle kann Text zählen; Chatvorlage, Systemtext und Ausgabe verändern den vollständigen Bedarf zusätzlich. Prüfe die tatsächlichen Nutzungsfelder der Antwort. Füllzeilen zählen beweist kein220K-Ergebnis.

## 8. Kontext wie einen Arbeitstisch planen
Modellgewichte, Kontextzustand, Rechenpuffer, Windows und Anwendungen brauchen Speicher. Bei gemeinsamem RAM nutzt die GPU keinen unabhängigen zweiten Speicherpool. Mehr Slots, andere Quantisierung und Modellarchitektur verändern das Budget. Eine8GB-Karte ist nicht auf fünf Fragen begrenzt. 24GB oder32GB legen ebenfalls keine feste Tokenzahl fest. Hier wurde kein gemessener Direktvergleich dieser Karten durchgeführt.

## 9. Was der alte220K-Befund belegt
ARCHIV-BEFUND.json zeigt einen eigenen Lauf vom19.09.2026: Modellalias qwen3.8-27b-q4-voll,262144Kontext konfiguriert,219962Dokumenttokens,220101Prompttokens. Drei Codes kamen korrekt zurück. Die ursprüngliche Abnahme prüfte Code-Vorkommen; wir haben den erhaltenen Antwortinhalt jetzt zusätzlich offline als JSON exakt verglichen. Kein neuer Modelllauf fand statt.

## 10. Die entscheidende Cache-Grenze
Die alte Antwort meldet220097Prompttokens als gecacht, bei220101Prompttokens insgesamt. Die66,382Sekunden sind deshalb kein Kaltstart- oder Prefill-Rekord. Warmes Weiterarbeiten und erstmaliges Einlesen getrennt dokumentieren. Wir löschen dafür weder fremden Cache noch starten einen belegten Server neu. Bei fehlendem Cache-Feld bleibt dessen Zustand unbekannt; nicht automatisch kalt annehmen.

## 11. Erst dann schrittweise vergrößern
Du kannst später in einem neuen Zielordner mehr neutrale Zeilen erzeugen. Prüfe nach jedem tatsächlichen Lauf Codes, Nutzung, Speicher und Zeit. Die Obergrenze2000Zeilen ist ein bewusst kleiner Übungsrahmen, keine maximale Modellfähigkeit. Ein wirklich großer Lasttest braucht separat bestätigte Ressourcen und einen dokumentierten Aufruf. Seine Reproduktion verspricht dieses Paket nicht.

## 12. Einen brauchbaren Befund sichern
Fülle PRUEFPROTOKOLL.csv mit tatsächlichem Modell, Quantisierung, Backend, Kontext, Slots, Nutzungszahlen, Cachezustand, Zeit und Grenzen aus. Drei richtige Markierungen sind eine nützliche begrenzte Prüfung, keine Zusage, dass ein Agent jede Aufgabe löst. Speichere Rohantwort und Quellen. Vorbereitung, eigene Prüfertests, Modellantwort und fachliches Urteil bleiben getrennte Schritte. Andere AMD-PCs oder Macs sind hier nicht frisch erprobt.
