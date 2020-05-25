import numpy as np
import sys
from studentSeed import studentSeed
from generateData_base import generateLinearData
from scipy import constants

experiment = "V4041"
name = sys.argv[1]
workingDir = experiment + "/" + name + "/"
seed = studentSeed(name)
np.random.seed(seed)


def getImageDistance(objectDistance, refractivity, noiseStd=0.1):
    """
    Args:
    objectDistance (Array)
    refractivity (float)
    noiseStd (float) (default: 0.1)

    Returns:
    imageDistance (Array)
    """
    if not isinstance(objectDistance, np.ndarray):  # to get the len()
        objectDistance = np.array([objectDistance])
    return (1 / (refractivity - 1 / objectDistance)
            + np.random.normal(0, noiseStd, len(objectDistance)))

# _____________________________________________________________________________
# V40
# _____________________________________________________________________________
# Part 1: two collecting lenses separately
# objectDistance [m]
# imageDistance [m]
# focusDistance [m]
# refractivity [dpt]


# lens 1, refractivity D1 = 10 dpt
objectDistance1 = np.array([25, 30, 35, 40]) * 1e-2
imageDistance1 = getImageDistance(objectDistance1, 10, 0.02)
# save it in [cm]
np.save(workingDir + "Data" + experiment + "Part1_Lens1",
        np.round(np.array([objectDistance1 * 1e2, imageDistance1 * 1e2]), 1))

# lens 2, refractivity D2 = 3.5 dpt
objectDistance2 = np.array([55, 60, 65, 70]) * 1e-2  # cm -> m
imageDistance2 = getImageDistance(objectDistance2, 3.5, 0.06)
# save it in [cm]
np.save(workingDir + "Data" + experiment + "Part1_Lens2",
        np.round(np.array([objectDistance2 * 1e2, imageDistance2 * 1e2]), 1))

# _____________________________________________________________________________
# Part 2: two collecting lenses together, refractivity D3 = 13 dpt
# distance between lenses = 3cm
objectDistance3 = 0.15
imageDistance3 = getImageDistance(objectDistance3, 13, 0.02)
# save it in [cm]
np.save(workingDir + "Data" + experiment + "Part2",
        np.round(np.array([objectDistance3 * 1e2, imageDistance3 * 1e2], dtype=np.float), 1))

# _____________________________________________________________________________
# Part 3: diffuser lens
# combined with lens 1, refractivity D4 = 3.3 dpt
# distance between lenses = 3cm
objectDistance4 = 0.50
imageDistance4 = getImageDistance(objectDistance4, 3.3, 0.08)
np.save(workingDir + "Data" + experiment + "Part3",
        np.round(np.array([objectDistance4 * 1e2, imageDistance4 * 1e2], dtype=np.float), 1))


# _____________________________________________________________________________
# V41
# _____________________________________________________________________________
# Near point, refractivity = 9
objectDistanceNearPoint = 0.3 + np.random.normal(0, 0.10)
imageDistanceNearPoint = getImageDistance(objectDistanceNearPoint, 9, 0.10)
# save it in [cm]
np.save(workingDir + "Data" + experiment + "Part4Near",
        np.round(np.array([objectDistanceNearPoint * 1e2, imageDistanceNearPoint * 1e2],
                          dtype=np.float), 1))

# _____________________________________________________________________________
# Far point, refractivity = 7
objectDistanceFarPoint = 0.3 + np.random.normal(0, 0.10)
imageDistanceFarPoint = getImageDistance(objectDistanceFarPoint, 7, 0.10)
# save it in [cm]
np.save(workingDir + "Data" + experiment + "Part4Far",
        np.round(np.array([objectDistanceFarPoint * 1e2, imageDistanceFarPoint * 1e2],
                          dtype=np.float), 1))
