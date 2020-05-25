import numpy as np
import sys
from studentSeed import studentSeed

experiment = "V42"
name = sys.argv[1]
workingDir = experiment + "/" + name + "/"
seed = studentSeed(name)
np.random.seed(seed)

# _____________________________________________________________________________
# Part 1: Refraction index (n = 1.5)
# alphas [degree]
# betas [degree]
# angleOfTotalReflection [degrees]

alphas = np.linspace(30, 50, 5)
betas = np.degrees(np.arcsin(np.sin(np.radians(alphas) / 1.5))) + \
    np.random.normal(0, 0.5, len(alphas))

np.save(workingDir + "Data" + experiment + "Part1",
        np.round(np.array([alphas, betas]), 1))

angleOfTotalReflection = np.degrees(
    np.arcsin(1 / 1.5)) + np.random.normal(0, 0.5)

np.save(workingDir + "Data" + experiment + "angleOfTotalReflection",
        np.round(angleOfTotalReflection, 1))
