## Moodle submissions util

> **Idee:** Der Sinn dieses Programms ist es, die Abgaben einer Aufgabe aus Moodle nach Teilnehmer zu sortieren. 

Wenn bei Moodle alle Abgaben heruntergeladen werden, bekommt man eine Zip-Datei, die für jede Abgabe einen Ordner mit dem Namen `Vorname Nachname_Ordnungsmerkmal_assignsubmission_file_` enthält. Dieses Programm erstellt verschiedene Unterordner, sortiert die Abgaben darein und löscht nichtmehr benötigte Abgaben. Dafür werden verschiedene Teilnehmerlisten in txt-Format benötigt – es können beliebig viele sein. 

### Benutzung

1. Git-Repository clonen

```{Shell}
git clone git@github.com:valentin-carl/moodlesubmissions.git
```

2. Teilnehmerlisten aktualisieren

Im Ordner `Teilnehmer` sind zwei Teilnehmerlisten als Beispiel enthalten. Hier entsprechend viele Listen (eine pro Lab) anlegen und die Teilnehmer so wie die Beispiele eintragen. Wichtig: Der Name der Person muss vollständig sein bzw. so wie der Moodle Name sein, damit die Abgabe nicht aussortiert wird.

3. Alle Abgaben von Moodle herunterladen

Dafür auf die entsprechende Aufgabe bei Moodle gehen, das Zahnrad anklicken und „Alle Abgaben herunterladen” anklicken. Dann die Zip-Datei entpacken (Safari tut dies automatisch) und den Inhalt in den Abgabenordner schieben. Diese Repo enthält bereits ein Bespiel dafür, wie dies aussehen soll.

4. Programm ausführen

```{Shell}
python3 sort.py
```

Die Schritte 1 und 2 müssen nur beim ersten Mal ausgeführt werden. Für jede neue Abgabe danach müssen nur die Abgaben in den Abgabenordner eingefügt und das Programm ausgeführt werden. Es wird dann jedes Mal ein neuer Ordner für die neue Woche erstellt, die alten Ordner können einfach an derselben Stelle beleiben (sollten sie auch, damit die Nummerierung der Wochen passt). 
