# computerspende

Script zu Erfassung unserer Geräte in Mantis.

Ziel ist es, dass Neueinsteiger oder Leute, die es nicht so oft machen, auch eine Chance haben
den Ablauf richtig hinzubekommen.

## Anforderungen:

* Das Script läuft auf unserem Standard Image ohne zusätzliche Software
=> Shellscript oder Python denke ich, anderes gerne willkommen

* Das Einstiegs-Script lädt sich von assets.computerspende-regensburg.de das eigentliche script herunter, so bekommen wir updates hin ohne das jeder immer alles austauschen muss

* Das heruntergeladene wird ausgeführt und ermittelt die Daten für den Eintrag (siehe nächster Punkt)

* Das Script erzeugt einen Mantis-Eintrag über die Mantis Rest-API:
https://documenter.getpostman.com/view/29959/mantis-bug-tracker-rest-api/7Lt6zkP#intro

Gefüllt ist:
- Reporter (Benutzername und Passwort muss übergeben werden),
- Betriebssystem,
- RAM,
- WLAN,
- Webcam,
- CPU,
- eine schöne "Zusammenfassung",
- Plattengröße (inkl. SSD oder HDD Anmerkung)
- Standort = Benutzername (falls es den nicht gibt für einen Benutzernamen, kann ich ihn anlegen)
- Welches OS installiert ist

* Schöne Wrapper Scripte vorbereitet:
  - createAndFinish: Legt den Mantis-Eintrag an und füllt o. g. Felder und setzt den Status dann gleich auf "erledigt"
  - create: Legt nur einen neuen Eintrag an mit allem was ermittelbar ist und setzt ihn auf "zugewiesen"
