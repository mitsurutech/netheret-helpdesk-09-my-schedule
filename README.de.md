# Netheret-Helpdesk, Schritt 09: Mein Plan

[English](README.md) | [Français](README.fr.md) | [Español](README.es.md) | [日本語](README.ja.md) | [Deutsch](README.de.md)

Ein Beispiel für den Unterricht. In sechzehn Schritten bauen wir eine Helpdesk-Webanwendung für Netheret, ein erfundenes Unternehmen, das die IT kleiner Firmen betreut. Dieser Schritt gibt Technikern in Tier 2 und Tier 3 ihren eigenen Plan und zu jedem Einsatz einen Einsatzauftrag, in dem sie ihren Fortschritt festhalten.

## Was dieser Schritt hinzufügt

In `helpdesk/jobs.py`:

- `/jobs/mine`: die Einsätze eines Technikers ab heute, nach Tagen gruppiert, dazu
  jeder ältere Einsatz, der noch als „in progress“ markiert ist.
- `/jobs/<id>`: der Einsatzauftrag: wann, wo, die Telefonnummer des Kunden, die
  Aufgabe und, wenn der Einsatz aus einer Anfrage stammt, das ursprüngliche Problem des Kunden.
- `/jobs/<id>/progress`: Der Techniker setzt den Einsatz auf „in progress“ oder
  „done“ und schreibt Notizen. Wenn ein Einsatz aus einer Anfrage erledigt ist, kommt eine Notiz in
  den Verlauf dieser Anfrage.

In `helpdesk/models.py` halten `Job.can_be_seen_by()` und `Job.can_be_updated_by()`
die Regeln, wer einen Einsatz sehen und ändern darf, an einer Stelle fest. Die Wochenansicht
und die Seite des Einsatzauftrags verwenden sie beide.

## Starten

```
python -m venv .venv
source .venv/bin/activate        # on Windows: .venv\Scripts\activate
pip install -r requirements.txt
python seed.py
flask --app helpdesk run --debug
```

Melden Sie sich als `tier2@netheret.example` oder `tier3@netheret.example` an (Demo-Passwort
`password123`) und öffnen Sie My schedule. Versuchen Sie, den Einsatz eines anderen
Technikers aus der Wochenansicht zu öffnen: Es gibt keinen Link, und wer die Adresse eintippt,
erhält 403.

## Worauf Sie achten sollten

- `days.setdefault(day, []).append(job)`: eine kurze Art, eine Liste zu einem
  Dictionary von Listen zu gruppieren.
- Ein Techniker kann einen Einsatz nicht stornieren. Das Formular bietet diese Wahl nicht an, und der
  Server lehnt sie ebenfalls ab, denn wer ein Formular benutzt, kann es verändern.
- `finished_now`: Die Notiz im Verlauf wird nur geschrieben, wenn ein Einsatz zum ersten Mal
  erledigt ist, nicht bei jedem Speichern der Notizen.

## Diesen Schritt lernen

Dies ist Schritt 9 von 16 aus **Task 2. Developing the solution**, einer kostenlosen Reihe von Lektionen zu T Level Digital Software Development auf Englisch, die den Helpdesk von Netheret in agilen Sprints mit Python und Flask baut. Lesen Sie die Lektion zu diesem Schritt:
[Der Plan eines Technikers und die Einsatzaufträge](https://mitsurutech.co.uk/resources/t-level/dsd-t2-09-my-schedule).

- Vorheriger Schritt: [Schritt 08, Vor-Ort-Einsätze planen](https://github.com/mitsurutech/netheret-helpdesk-08-jobs)
- Nächster Schritt: [Schritt 10, Die Wissensdatenbank](https://github.com/mitsurutech/netheret-helpdesk-10-knowledge-base)
- [Alle kostenlosen Lektionen zu T Level Digital](https://mitsurutech.co.uk/resources/t-level)
- [Diese Lektionen mit Ihrer Klasse auf MitsuruTech unterrichten](https://mitsurutech.co.uk/de/learning), [die Preise ansehen](https://mitsurutech.co.uk/de/pricing) oder
  [ein kostenloses Jahr für Ihre Schule beginnen](https://mitsurutech.co.uk/de/signup)

## Über dieses Beispiel

Geschrieben von [Mitsuru Technologies](https://mitsurutech.co.uk/de) (MitsuruTech) als Unterrichtsbeispiel für T Level Digital
Software Development. Die Aufgabenstellung Netheret IT Support Solutions stammt aus dem Muster-Prüfungsmaterial von Pearson; dieser Code
und seine Erläuterungen sind unsere eigenen und werden weder von Pearson noch vom Department for Education veröffentlicht, unterstützt oder genehmigt.
„T Level“ ist eine eingetragene Marke des Department for Education.
