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

## Einrichtung einer Mantis Docker Umgebung (funktioniert aktuell nicht)

### docker-compose.yml
``` yaml
version: '3'
services:

  mysql:
    image: mysql:5.7
    container_name: mysql
    environment:
      - MYSQL_ROOT_PASSWORD=root
      - MYSQL_DATABASE=mantis
      - MYSQL_USER=mantisbt
      - MYSQL_PASSWORD=mantisbt
    restart: always

  phpmyadmin:
    image: phpmyadmin
    container_name: phpmyadmin
    environment:
      - PMA_HOST=mysql
      - MYSQL_ROOT_PASSWORD=root
    restart: always
    ports:
      - 8080:80
    volumes:
      - /sessions
    depends_on:
      - mysql

  mantisbt:
    image: vimagick/mantisbt:latest
    container_name: mantisbt
    restart: always
    ports:
      - "8989:80"
    depends_on:
      - mysql
networks:
  mantis:

```
### Diese Vorgehensweise:

1. docker-compose up -d
2. In phpmyadmin unter zB 192.168.236.2:8080 einloggen mit mantisbt und mantisbt, Datenbank mantis erstellen
3. Import des sql dump in phpmyadmin in die Datenbank mantis oder über mysql -u root -p mantis < export_mantis_db.sql
4. docker-compose -f docker-compose.yml exec mysql /bin/bash
	1. mysql -u root -p mantis (passwort ist root)
	2. 	;
5. dann http://192.168.236.2:8989/admin/install.php aufrufen und
Eintragen:
- hostname: mysql
- user: mantisbt
- passworduser: mantisbt
- datenbank: mantis

- admin: root
- password: root

Die restliche Felder entsprechen den Default Werten

### Ergibt folgenden Fehler:
```
Fatal error: 401 in /var/www/html/core/classes/DbQuery.class.php on line 293
```
=> Funktioniert jetzt, aber es gibt kein Zugriff auf die Datenbank...
Anscheinend liest er nicht die mantis datenbank aus sondern verwendet irgenwas anderes evtl. eine andere default datenbank. Denn Benutzer administrator und root ist vorhanden...

### Wenn nix geht => Löschen und von neuem Starten
1. docker-compose down
2. sudo rm -rf data
3. armageddon (is bei mir in der bashrc n commando um alles was mit docker zu tun hat zu löschen)

### Einspielen des sql dumps über cli:
mysql -u root -p bugtracker < export_mantis_db.sql

### Links:

Startpage search:
Does administrative user have access to the database? ( No such file or directory )

https://github.com/xlrl/docker-mantisbt/issues/4


Das ganze Ding funktioniert nicht...komplett nervig und frustrierend.
Evtl. tue ich das mal irgendwo dokumentieren. 
### Manueller Vorgang:


https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-phpmyadmin-on-ubuntu-20-04-de

Zusätzlicher Nutzer für phpmyadmin einrichten in mysql.

CREATE USER 'mantisbt'@'localhost' IDENTIFIED BY 'mantisbt';

Rechte vergeben
GRANT ALL PRIVILEGES ON *.* TO 'mantisbt'@'localhost' WITH GRANT OPTION;
flush privileges;

Falls notwendig, Rechte auf die Mantis db dem root User geben:
GRANT ALL PRIVILEGES ON mantis to root@'localhost' IDENTIFIED BY 'root'; flush privileges;

Alternativ kann man auch dem root Nutzer Passwortzugriff geben auf die DB

UPDATE mysql.user SET plugin = 'mysql_native_password' WHERE user = 'root' AND plugin = 'unix_socket';

https://www.bennetrichter.de/anleitungen/apache2-php7-mariadb-phpmyadmin/

So manuell gehts auch nicht.
Liegt wohl an den Rechten.

https://websolutionstogo.de/blog/mantis-bug-tracker-installation-update/

Import dump
https://mantisbt.org/forums/viewtopic.php?t=20592
https://www.mantisbt.org/forums/viewtopic.php?t=26850
https://www.mantisbt.org/wiki/doku.php/mantisbt:db_dump_restore

https://docs.bitnami.com/installer/apps/mantis/administration/backup-restore-mysql-mariadb/
https://docs.bitnami.com/installer/apps/mantis/administration/export-database/

Mount a directory to docker compose
https://stackoverflow.com/questions/40905761/how-do-i-mount-a-host-directory-as-a-volume-in-docker-compose

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
Hier sieht man den erstellten Token, man kann ihn mit einem Klick auf Revoke wieder löschen
<img width="1680" alt="TokenErstellung5" src="https://user-images.githubusercontent.com/19862760/106341772-ba024d80-629e-11eb-819d-adf4a71f71bc.png">
