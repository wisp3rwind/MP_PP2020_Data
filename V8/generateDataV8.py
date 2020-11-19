import numpy as np
import sys
from studentSeed import studentSeed
from generateData_base import generateLinearData

experiment = "V8"
name = sys.argv[1]
workingDir = experiment + "/" + name + "/"
seed = studentSeed(name)
np.random.seed(seed)

# _____________________________________________________________________________
# Part 1: Quincks pipe

# resonanceLengths [cm]
# To get the speed of sound of c=330ms slope should be 8.25,
# but the last experiments had a lower value here
nMeasurement = np.arange(1, 12)
resonanceLengths = generateLinearData(
    nMeasurement, slope=8.57, intercept=0, noiseStd=1, roundTo=1)

np.save(workingDir + "Data" + experiment + "Part1", resonanceLengths)

# _____________________________________________________________________________

# Part 2: Ultrasonic

# waveLengths [mm]
waveLengths = generateLinearData(
    nMeasurement, slope=8.25, intercept=0, noiseStd=1, dtype=np.int)

np.save(workingDir + "Data" + experiment + "Part2", waveLengths)

# _____________________________________________________________________________
# Part 3: Sonar

# distances (one way) [mm]
# times [ms] (two way!)
distances = np.linspace(100, 800, 8)
times = generateLinearData(
    distances, slope=2/340., intercept=0, noiseStd=0.3, roundTo=2)
# avoid times less than 0.1 ms
times = np.maximum(times, 0.1)

np.save(workingDir + "Data" + experiment +
        "Part3", np.array([distances, times]))
