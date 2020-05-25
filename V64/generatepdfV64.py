import generatepdf_base as gpdf
import sys
import numpy as np

name = sys.argv[1]
experiment = "V64"
workingDir = experiment + "/" + name + "/"

gpdf.addText("Versuchsdaten für " + name.replace('_', ' '))
gpdf.addText("Versuch Nummer " + experiment[1:])
gpdf.addSpacer()

gpdf.addText("Bestimmung der Schächungskoeffizienten")
gpdf.addText("Aluminium:")
header = [["Absorberdicke [cm]", "Pulszahl"]]
data1 = np.load(workingDir + "DataV64Alu.npy").T
gpdf.addTable(header, data1)
gpdf.addSpacer()

gpdf.addText("Kupfer")
data2 = np.load(workingDir + "DataV64Cu.npy").T
gpdf.addTable(header, data2)
gpdf.addSpacer()

gpdf.createPDF(experiment, name)
