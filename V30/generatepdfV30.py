import generatepdf_base as gpdf
import numpy as np
from get_students import get_students

students = get_students()
experiment = "V30"

for student in students:
    workingDir = experiment + "/" + student + "/"

    gpdf.addText("Versuchsdaten für " + student.replace('_', ' '))
    gpdf.addText("Versuch Nummer " + experiment[1:])
    gpdf.addSpacer()

    gpdf.addText("Teil 3: Bestimmung von e/m")
    header3 = [["Spannung [V]", "Strom [A]", "Durchmesser [cm]"]]
    data3 = np.load(workingDir + "DataV30Part1.npy").T
    gpdf.addTable(header3, data3)

    gpdf.addPagebreak()

gpdf.createPDF(experiment)
