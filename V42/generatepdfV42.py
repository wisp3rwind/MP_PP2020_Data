import generatepdf_base as gpdf
import numpy as np
from get_students import get_students

students = get_students()
experiment = "V42"

for student in students:
    workingDir = experiment + "/" + student + "/"

    gpdf.addText("Versuchsdaten für " + student.replace('_', ' '))
    gpdf.addText("Versuch Nummer " + experiment[1:])
    gpdf.addSpacer()

    gpdf.addText("Teil 1: Brechungsindex")
    header1 = [["α [Grad]", "β [Grad]"]]
    data1 = np.load(workingDir + "DataV42Part1.npy").T
    gpdf.addTable(header1, data1)
    gpdf.addSpacer()

    angleOfTotalReflection = str(
        np.load(workingDir + "DataV42angleOfTotalReflection.npy"))
    gpdf.addText("Winkel der Totalreflektion = {0}°".format(
        angleOfTotalReflection))
    gpdf.addSpacer()
    gpdf.addSpacer()

    gpdf.addText("Teil 2: Kalibrierung mit Spektrallinien von Helium")
    header2 = [["Skala", "Wellenlänge [nm]", "Farbe"]]
    data2 = np.load(workingDir + "DataV42Part2.npy").T
    gpdf.addTable(header2, data2)
    gpdf.addSpacer()
    gpdf.addSpacer()

    gpdf.addText("Teil 3: Bestimmung der Spektrallinien von Neon")
    header3 = [["Skala", "Farbe"]]
    data3 = np.load(workingDir + "DataV42Part3.npy").T
    gpdf.addTable(header3, data3)

    gpdf.addPagebreak()

gpdf.createPDF(experiment)
