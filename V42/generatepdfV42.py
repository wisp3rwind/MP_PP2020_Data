import generatepdf_base as gpdf
import sys
import numpy as np

name = sys.argv[1]
experiment = "V42"
workingDir = experiment + "/" + name + "/"

gpdf.addText("Versuchsdaten für " + name.replace('_', ' '))
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

gpdf.createPDF(experiment, name)
