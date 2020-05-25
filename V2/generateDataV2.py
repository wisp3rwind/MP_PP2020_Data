import numpy as np
import sys
sys.path.insert(0,'/Users/markuswalther/work/Data/Data')
print(sys.path)

from studentSeed import studentSeed
from generateData_base import generateLinearData

experiment = "V2"
name = sys.argv[1]
workingDir = experiment + "/" + name + "/"
seed = studentSeed(name)
np.random.seed(seed)

# _____________________________________________________________________________
# Part 1, static measurement

# masses [g]
# slope [mm/g]
# intercept [mm]
# noiseStd [mm]
# lengths [mm]

masses = np.linspace(10, 50, 5, dtype=np.int)
# int_ is important for the printout later
# the pdf displays '10' instead of '10.0' with this option

lengths = generateLinearData(
    masses, slope=3.4, intercept=196, noiseStd=10, dtype=np.int)

# save it to file
np.save(workingDir + "Data" + experiment + "Part1",
        np.array([masses, lengths]))

#  _____________________________________________________________________________
# Part 2, dynamic measurement

# masses [g]
# slope [s/g]
# intercept [s]
# noiseStd [s]
# periods [s]

# Its 10 times the arrays, since in the experimt, 10 periods are measured
#periods = generateLinearData(
#    masses, slope=0.011, intercept=0.28, noiseStd=0.08, roundTo=3) * 10
periods = np.round(np.sqrt(generateLinearData(
    masses, slope=0.0134, intercept=0.02, noiseStd=0.02, roundTo=5)) * 10,2)

masses=masses.astype(int)
# save it to
np.save(workingDir + "Data" + experiment + "Part2",
        np.array([masses, periods]))
