import numpy as np
import sys
from studentSeed import studentSeed
from generateData_base import generateExpoData

experiment = "V64"
name = sys.argv[1]
workingDir = experiment + "/" + name + "/"
seed = studentSeed(name)
np.random.seed(seed)

# _____________________________________________________________________________
# Part 1: Determination of the decreasing coefficiant
# µ_alu = 0.15 cm−1, µ_cu = 0.6 cm-1

# x_alu [mm]
# x_cu [mm]
# N_alu
# N_cu

# counts with no material in between
# and make sure its not too low
# and not above 1000 to fit on the linlog-paper
# N0 = max(1000 + np.random.normal(0, 200), 321)
N0 = min(max(1000 + np.random.normal(0, 200), 321),990)

# Nbg = background counts with Geiger-counter totally blocked
Nbg = int(np.round(max(np.random.normal(20, 5), 5)))

np.save(workingDir + "DataV64Nbg",Nbg)

# alu
mu_alu = -0.15
x_alu = np.linspace(5, 40, 8, dtype=np.int)
N_alu = generateExpoData(x_alu * 1e-3, N0, mu_alu *
                         1e2, noiseStd=0.1, dtype=np.int) + Nbg

np.save(workingDir + "DataV64Alu", np.array([x_alu, N_alu], dtype=np.int))

mu_cu = -0.6
x_cu = np.linspace(3, 30, 10, dtype=np.int)
N_cu = generateExpoData(x_cu * 1e-3, N0, mu_cu * 1e2,
                        noiseStd=0.1, dtype=np.int) + Nbg

np.save(workingDir + "DataV64Cu", np.array([x_cu, N_cu], dtype=np.int))
