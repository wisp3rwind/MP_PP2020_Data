import generatepdf_base as gpdf
import numpy as np
from get_students import get_students

students = get_students()
experiment = "V39"

for student in students:
    workingDir = experiment + "/" + student + "/"

    gpdf.addText("Versuchsdaten für " + student.replace('_', ' '))
    gpdf.addText("Versuch Nummer " + experiment[1:])
    gpdf.addSpacer()

    gpdf.addText("Teil 1: Kohlepapierstreifen")
    gpdf.addSpacer()
    gpdf.addText("Kontaktklemme (-) bei x = 15 cm")
    gpdf.addText("Kontaktklemme (+) bei x = 35 cm")
    gpdf.addSpacer()
    header1 = [["Position x [cm]", "Spannung [V]"]]
    data1 = np.load(workingDir + "DataV39Part1.npy").T
    gpdf.addTable(header1, data1)
    gpdf.addSpacer()
    gpdf.addSpacer()
    gpdf.addSpacer()
    gpdf.addSpacer()
    gpdf.addSpacer()
    gpdf.addSpacer()

    gpdf.addText("Teil 3: EKG-Ableitung")
    gpdf.addSpacer()
    header2 = [["Winkel [Grad]", "Spannung R&L [V]",
                "Spannung L&F [V]", "Spannung F&R [V]"]]
    data2 = np.load(workingDir + "DataV39Part2.npy").T
    gpdf.addTable(header2, data2)
    gpdf.addSpacer()

    gpdf.addPagebreak()

gpdf.createPDF(experiment)
