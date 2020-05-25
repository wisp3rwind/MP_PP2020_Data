import generatepdf_base as gpdf
import sys
import numpy as np

name = sys.argv[1]
experiment = "V39"
workingDir = experiment + "/" + name + "/"

gpdf.addText("Versuchsdaten für " + name.replace('_', ' '))
gpdf.addText("Versuch Nummer " + experiment[1:])
gpdf.addSpacer()

gpdf.addText("Teil 1: Kohlestreifen")
header1 = [["Abstaende [cm]", "Spannung [V]"]]
data1 = np.load(workingDir + "DataV39Part1.npy").T
gpdf.addTable(header1, data1)
gpdf.addSpacer()

gpdf.addText("Teil 3: EKG-Ableitung")
header2 = [["Winkel [Grad]", "Spannung R&L [V]",
            "Spannung L&F [V]", "Spannung F&R [V]"]]
data2 = np.load(workingDir + "DataV39Part2.npy").T
gpdf.addTable(header2, data2)
gpdf.addSpacer()

gpdf.createPDF(experiment, name)
