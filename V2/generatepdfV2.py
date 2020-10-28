import generatepdf_base as gpdf
import numpy as np
from get_students import get_students

students = get_students()
experiment = "V2"

for student in students:
    workingDir = experiment + "/" + student + "/"

    gpdf.addText("Versuchsdaten für " + student.replace('_', ' '))
    gpdf.addText("Versuch Nummer " + experiment[1:])
    gpdf.addSpacer()

    gpdf.addText("Teil 1: Statische Messung")

    header1 = [["Massen [g]", "Laengen [mm]"]]
    data1 = np.load(workingDir + "DataV2Part1.npy").T
    gpdf.addTable(header1, data1)

    gpdf.addSpacer()
    gpdf.addText("Teil 2: Dynamische Messung")

    header2 = [["Massen [g]", "10 Perioden [s]"]]
    data2 = np.load(workingDir + "DataV2Part2.npy").T
    gpdf.addTable(header2, data2)

    gpdf.addPagebreak()

gpdf.createPDF(experiment)
