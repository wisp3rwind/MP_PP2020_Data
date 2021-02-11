Datengenerierungsprogramm für Med/Dent Physikpraktikum SS2020
=============================================================

1. Benutzung:

    1.  Die Datei "students.txt" mit namen der studenten füllen, Vorname(n) Nachname mit Leerzeichen getrennt, bspw.:
    Max Mustermann
    Karl-Theodor Maria Nikolaus Johann Jacob Philipp Franz Joseph Sylvester Buhl-Freiherr von und zu Guttenberg

    2. "python3 main.py" ausführen.

        Dadurch wird für jeden Student für jedes Experiment
        * Ein Ordner mit "Experiment/Studentenname" erstellt
        * Daten generiert aufgrund des Namen des Studenten als "random seed", damit es reproduzierbar ist
        * Ein PDF der daten für ILIAS erstellt
        * Ein Auswertungsnotebook in das Verzeichnis kopiert

    3. Zum löschen aller Studentendaten "python3 clearData.py" ausführen.


2. Benötigte Packages: NumPy, SciPy, MatplotLib, ReportLab, os, shutil, sys
   Sollte alles standardmäßig vorhanden sein.

3. Bekannte Fehler: Bei der Konversation von float -> string kommt es manchmal dazu, dass z.b. 12.3 dann als "12.2999999999999993" oder "12.30000000000000003" angegeben wird. Ist ein bisschen hässlich.
