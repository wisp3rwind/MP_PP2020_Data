import numpy as np
import sys
from studentSeed import studentSeed
from generateData_base import generateLinearData, generateSinusData

experiment = "V39"
name = sys.argv[1]
workingDir = experiment + "/" + name + "/"
seed = studentSeed(name)
np.random.seed(seed)

# _____________________________________________________________________________
# Part 1: Carbon strip

# distances [cm]
# voltage [V]
#distances = np.linspace(0, 20, 21)
distances = np.linspace(0, 50, 26)
distances2 = np.linspace(16, 34, 10)
distances3 = np.linspace(36, 50, 8)
#voltages = generateLinearData(distances, slope=0.25, intercept=0, noiseStd=0.1, roundTo=2)
voltages1 = np.array([0, 0, 0, 0, 0, 0, 0, 0])
voltages2 = generateLinearData(distances2, slope=0.247, intercept=-3.7, noiseStd=0.015, roundTo=2)
voltages3 = generateLinearData(distances3, slope=-0.005, intercept=5.1, noiseStd=0.015, roundTo=2)
voltages = np.append(voltages1, np.append(voltages2, voltages3))

np.save(workingDir + "Data" + experiment +
        "Part1", np.array([distances, voltages]))

# _____________________________________________________________________________
# Part 2
angles = np.linspace(0, 2 * np.pi, 19)
angles_in_degree = np.linspace(0, 360, 19)
UPosition1 = generateSinusData(angles, amplitude=0.3, offsetAngle=0,
                               noiseStd=0.02, roundTo=2)
UPosition2 = generateSinusData(angles, amplitude=0.3, offsetAngle=2 * np.pi/3,
                               noiseStd=0.02, roundTo=2)
UPosition3 = generateSinusData(angles, amplitude=0.3, offsetAngle=4 * np.pi/3,
                               noiseStd=0.02, roundTo=2)

np.save(workingDir + "Data" + experiment + "Part2",
        np.array([np.round(angles_in_degree,0), UPosition1, UPosition2, UPosition3]))
