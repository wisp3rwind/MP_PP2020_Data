import generatepdf_base as gpdf
import sys
import numpy as np

name = sys.argv[1]
experiment = "V4041"
workingDir = experiment + "/" + name + "/"

gpdf.addText("Versuchsdaten für " + name.replace('_', ' '))
gpdf.addText("Versuch Nummer " + "40")
gpdf.addSpacer()

gpdf.addText("Teil 1: Sammellinsen")
gpdf.addText("Linse 1:")
header = [["Bildweite [cm]", "Gegenstandsweite [cm]"]]
data11 = np.load(workingDir + "DataV4041Part1_Lens1.npy").T
gpdf.addTable(header, data11)
gpdf.addText("Linse 2:")
data12 = np.load(workingDir + "DataV4041Part1_Lens2.npy").T
gpdf.addTable(header, data12)
gpdf.addSpacer()

gpdf.addText("Teil 2: Linsensystem")
gpdf.addText("Linse 1 + Linse 2:")
gpdf.addText("Linsenabstand = 2.8 cm")
data2 = np.load(workingDir + "DataV4041Part2.npy").T
gpdf.addTable(header, [data2])
gpdf.addSpacer()

gpdf.addText("Teil 3: Zerstreulinse")
gpdf.addText("Linse 1 + Linse 3:")
gpdf.addText("Linsenabstand = 3.0 cm")
data3 = np.load(workingDir + "DataV4041Part3.npy").T
gpdf.addTable(header, [data3])
gpdf.addSpacer()

#gpdf.addText("Nahpunkt:")
#data4Near = np.load(workingDir + "DataV4041Part4Near.npy").T
#gpdf.addTable(header, [data4Near])
#gpdf.addText("Fernpunkt:")
#data4Far = np.load(workingDir + "DataV4041Part4Far.npy").T
#gpdf.addTable(header, [data4Far])

gpdf.createPDF(experiment, name)
