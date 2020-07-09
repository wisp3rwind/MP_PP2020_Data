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
#betas = np.degrees(np.arcsin(np.sin(np.radians(alphas) / 1.5))) + np.random.normal(0, 0.5, len(alphas))
betas = (np.arcsin(np.sin(alphas* np.pi /180) / 1.5))*180/ np.pi + np.random.normal(0, 0.5, len(alphas))

np.save(workingDir + "Data" + experiment + "Part1",
        np.round(np.array([alphas, betas]), 1))

angleOfTotalReflection = np.degrees(
    np.arcsin(1 / 1.5)) + np.random.normal(0, 0.5)

np.save(workingDir + "Data" + experiment + "angleOfTotalReflection",
        np.round(angleOfTotalReflection, 1))


# _____________________________________________________________________________
# Part 2: Spectroscopy
# Skala [Skalenstriche]
# Linien [nm]

HeSkala = [5.8, 6.2, 7.2, 8.9, 9.1, 9.8, 10.7]
HeLinien = [707, 668, 588, 501, 492, 471, 447]
HeFarben = ["dunkelrot", "rot", "gelb", "grün", "blaugrün", "blau", "blau"]

np.save(workingDir + "Data" + experiment + "Part2",
        np.array([HeSkala, HeLinien, HeFarben]))

NeSkala = [5.8, 6.4, 6.6, 6.7, 6.8, 7.0, 7.3, 8.1]
NeFarben = ["dunkelrot", "dunkelrot", "rot", "rot", "rot", "orange", "gelb", "grün"]

np.save(workingDir + "Data" + experiment + "Part3",
        np.array([NeSkala, NeFarben]))
