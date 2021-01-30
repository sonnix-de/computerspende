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

## Deployment

[nylas.com](https://www.nylas.com/blog/packaging-deploying-python/)
```
pip install make-deb
```

## Anleitung zur Benutzung des Scripts
Als erstes erfolgt ein Klonen des Repository in einen Ordner. Am Sinnvollsten auf einer Partition des USB-Stick den man für das Klonen bzw. der Installation des Images auf den Rechnern verwendet. Per Defautl wird der Ordner computerspende am Ort erstellt wo der git clone Befehl aufgerufen wurde.
```
git clone https://github.com/sonnix-de/computerspende.git
```
Normalerweise sind python3, pip3 und die für das Skript benötigten Requirements bereits installiert. Falls es zu einer Fehlermeldung kommt, muss man diese Dinge erst noch installieren. Dazu lässt sich das mitgelieferte setup.sh verwenden:
```
chmod +x setup.sh
./setup.sh
```
Nun wird das Hauptskript gestartet
```
python3 main.py
```
Man wird nun aufgefordert den Mantis Token einzugeben. Wie dieser erstellt wird ist im Folgenden erklärt. Der Rest des Skriptes ist selbsterklärend, da ein Menü durch die einzelnen Schritte führt.

### Token erstellen
1. Erster Schritt Klick auf My Account oben rechts
<img width="1680" alt="TokenErstellung1" src="https://user-images.githubusercontent.com/19862760/106341766-b79ff380-629e-11eb-97b3-486f4d2b9031.png">
2. Klick auf API-Token (ist hier in blau markiert).
<img width="1680" alt="TokenErstellung2" src="https://user-images.githubusercontent.com/19862760/106341767-b8388a00-629e-11eb-99b4-ae18242c7fd0.png">
3. Nun einen Namen eingeben und auf Create API Token klicken.
<img width="1680" alt="TokenErstellung3" src="https://user-images.githubusercontent.com/19862760/106341770-b8d12080-629e-11eb-9b03-59e1e0147ab2.png">
4. Jetzt wird das folgende Fenster angezeigt. Den im grauen Bereich angezeigten Token -
Hier irgendwas mit S2R... - kopieren und in das Terminal Fenster in dem das python script geöffnet ist einfügen.
<img width="1680" alt="TokenErstellung4" src="https://user-images.githubusercontent.com/19862760/106341771-b969b700-629e-11eb-933a-8769cb807c6c.png">
### Token wieder löschen
1. Hier sieht man den erstellten Token
<img width="1680" alt="TokenErstellung5" src="https://user-images.githubusercontent.com/19862760/106341772-ba024d80-629e-11eb-819d-adf4a71f71bc.png">
2. Er lässt sich mit einem Klick auf Revoke wieder löschen
<img width="1680" alt="TokenLöschen" src="https://user-images.githubusercontent.com/19862760/106341773-ba024d80-629e-11eb-915e-1c12858fd52b.png">
