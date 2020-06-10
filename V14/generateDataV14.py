import numpy as np
import sys
from studentSeed import studentSeed
from generateData_base import generateLinearData

experiment = "V14"
name = sys.argv[1]
workingDir = experiment + "/" + name + "/"
seed = studentSeed(name)
np.random.seed(seed)

# _____________________________________________________________________________
# copper mass [g]
m_cu = 163 + np.random.normal(3)
# copper mass plus water mass [g]
m_ges = 230 + np.random.normal(5)
# temp before heating [°C]
T_1 = 21.6 + np.random.normal(0.5)
# temp after heating [°C]
T_2 = 25.6 + np.random.normal(0.5)
# diameter of the calorimeter [mm]
d = 47.8 + np.random.normal(2)

allData = [m_cu, m_ges, T_1, T_2, d]
np.save(workingDir + "Data" + experiment + "Part1", allData)
