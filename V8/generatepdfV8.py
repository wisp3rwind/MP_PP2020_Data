import generatepdf_base as gpdf
import sys
import numpy as np

name = sys.argv[1]
experiment = "V8"
workingDir = experiment + "/" + name + "/"


gpdf.addText("Versuchsdaten für " + name.replace('_', ' '))
gpdf.addText("Versuch Nummer " + experiment[1:])
gpdf.addSpacer()

gpdf.addText("Temperatur: 20°C")
gpdf.addSpacer()

gpdf.addText("Teil 1: Quincksches Rohr")
gpdf.addText("Lautsprecherfrequenz : 2 KHz")
header1 = ["Resonanzlaengen [cm]"]
data1 = np.load(workingDir + "DataV8Part1.npy").T
gpdf.addTable(header1, data1)
gpdf.addSpacer()

gpdf.addText("Teil 2: Ultraschall")
gpdf.addText("Ultraschallfrequenz: 40.692 KHz")
# Show only the last entry (after 10 wavelengths)
#gpdf.addText("Abstand zwischen 10 Wellenlaengen  : {} mm".format(
#    np.load(workingDir + "DataV8Part2.npy").T[-1]))
header2 = ["Wellenlaengen [mm]"]
data2 = np.load(workingDir + "DataV8Part2.npy").T
gpdf.addTable(header2, data2)
gpdf.addSpacer()

gpdf.addText("Teil 3: Echolot Verfahren")
header3 = [["Abstaende [mm]", "Zeiten [ms]"]]
data3 = np.load(workingDir + "DataV8Part3.npy").T
gpdf.addTable(header3, data3)

gpdf.createPDF(experiment, name)


gpdf.addText("Versuchsdaten für " + name.replace('_', ' '))
gpdf.addText("Versuch Nummer " + experiment[1:])
gpdf.addSpacer()

gpdf.addText("Temperatur: 20°C")
gpdf.addSpacer()

gpdf.addText("Teil 1: Quincksches Rohr")
gpdf.addText("Lautsprecherfrequenz : 2 KHz")
header1 = ["Resonanzlaengen [cm]"]
data1 = np.load(workingDir + "DataV8Part1.npy").T
gpdf.addTable(header1, data1)
gpdf.addSpacer()

gpdf.addText("Teil 2: Ultraschall")
gpdf.addText("Ultraschallfrequenz: 40.692 KHz")
# Show only the last entry (after 10 wavelengths)
gpdf.addText("Abstand zwischen 10 Wellenlaengen  : {} mm".format(
    np.load(workingDir + "DataV8Part2.npy").T[-1]))
# header2 = ["Wellenlaengen [mm]"]
# data2 = np.load(workingDir + "DataV8Part2.npy").T
# gpdf.addTable(header2, data2)
gpdf.addSpacer()

gpdf.addText("Teil 3: Echolot Verfahren")
header3 = [["Abstaende [mm]", "Zeiten [ms]"]]
data3 = np.load(workingDir + "DataV8Part3.npy").T
gpdf.addTable(header3, data3)

gpdf.createPDF(experiment, name)
