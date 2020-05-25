import generatepdf_base as gpdf
import sys
import numpy as np

name = sys.argv[1]
experiment = "V30"
workingDir = experiment + "/" + name + "/"

gpdf.addText("Versuchsdaten für " + name.replace('_', ' '))
gpdf.addText("Versuch Nummer " + experiment[1:])
gpdf.addSpacer()

gpdf.addText("Teil 3: Bestimmung von e/m")
header3 = [["Spannung [V]", "Strom [A]", "Durchmesser [cm]"]]
data3 = np.load(workingDir + "DataV30Part1.npy").T
gpdf.addTable(header3, data3)

gpdf.createPDF(experiment, name)
