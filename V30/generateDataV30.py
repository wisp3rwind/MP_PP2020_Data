import numpy as np
import sys
from studentSeed import studentSeed
from generateData_base import generateLinearData
from scipy import constants

experiment = "V30"
name = sys.argv[1]
workingDir = experiment + "/" + name + "/"
seed = studentSeed(name)
np.random.seed(seed)

e = constants.elementary_charge
m_e = constants.electron_mass


def B(I):
    return 0.78e-3 * I

# _____________________________________________________________________________
# voltage [V]
# current [A]
# radii [m]
# diameter [cm]


# 1. vary the voltage
voltage1 = np.linspace(200, 300, 5)
current1 = np.ones(5)
radii1 = np.sqrt(2 * voltage1 * m_e / (B(current1)**2 * e)
                 + np.random.normal(loc=0, scale=5e-4, size=len(voltage1)))

# 2. vary the current
voltage2 = np.ones(5) * 250
current2 = np.linspace(0.8, 1.8, 5)
radii2 = np.sqrt(2 * voltage2 * m_e / (B(current2)**2 * e)
                 + np.random.normal(loc=0, scale=5e-4, size=len(voltage2)))

voltage = np.concatenate((voltage1, voltage2))
current = np.concatenate((current1, current2))
# diameter in cm
diameter = np.round(np.concatenate((radii1, radii2)), 4) * 2 * 100

np.save(workingDir + "Data" + experiment + "Part1",
        np.array([voltage, current, diameter]))
