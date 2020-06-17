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
m_cu = 168 + np.random.normal(1)
# copper mass plus water mass [g]
m_ges = 224.8 + np.random.normal(1)
# temp before heating [°C]
T_1 = (214 + np.random.normal(1))/10
# temp after heating [°C]
T_2 = (262 + np.random.normal(1))/10
# diameter of the calorimeter [mm]
d = 47.8 + np.random.normal(0.3)

allData = [m_cu, m_ges, T_1, T_2, d]
np.save(workingDir + "Data" + experiment + "Part1", allData)
