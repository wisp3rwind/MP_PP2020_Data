import numpy as np


def generateLinearData(x, slope, intercept, noiseStd, roundTo=0, dtype=np.float):
    """
    Generates linear data with gaussian noise.

    Args:
    x (Array): input x array
    slope (float) (default 3.4): desired slope
    intercept (float) (default 196): desired intercept
    noiseStd (float) (default 10): the std of the gaussian noise added
                                   to the data
    roundTo (int) (default 0): round the result to the given digits
    dtype (type) (default np.float): dtype of return array

    Returns:
    yData (Array): The generated yData

    """
    return np.array(np.round(intercept + slope * x +
                             np.random.normal(
                                 loc=0, scale=noiseStd, size=len(x)),
                             decimals=roundTo), dtype=dtype)


def generateSinusData(angles, amplitude, offsetAngle=0, noiseStd=1, roundTo=0, dtype=np.float):
    """
    Generates sinus data with gaussian noise

    Args:
    angles (float): input angles in radiant
    amplitude (float)
    offsetAngle (float) (default 0)
    noiseStd (float) (default 1)
    roundTo (int) (default 0)
    dtype type (default np.float)

    Returns:
    sinusArray (Array): the resulting data

    """
    return np.array(np.round(amplitude * np.sin(angles + offsetAngle) +
                             np.random.normal(
                                 loc=0, scale=noiseStd, size=len(angles)),
                             decimals=roundTo), dtype=dtype)


def generateExpoData(x, N0, mu, noiseStd=0.1, roundTo=2, dtype=np.float):
    """
    Generates exponential decaying data with gaussian noise

    Args:
    x (Array): input array
    N0 (Float): start parameter
    mu (Float): decreasing parameter
    noiseStd (Float) (default 0.1): standard deviation of gaussian noise
    roundTo (int) (default 2)
    dtype type (default np.float)

    Returns:
    expoArray (Array): the resulting data
    """

    return np.array(np.round(N0 * np.exp(x * mu + np.random.normal(
        loc=0, scale=noiseStd, size=len(x))),
        decimals=roundTo), dtype=dtype)
