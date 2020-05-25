import matplotlib.pyplot as plt
from scipy.stats import linregress


def linearRegression(xdata, ydata, xlabel, ylabel):
    """
    Do a linear Regression with plotting

    Args:
    xdata (array): input x-array
    ydata (array): input y-array
    xlabel (string)
    ylabel (string)

    Returns:
    slope (float): the slope of the linear regression result
    intercept (float) the intercept of the linear regression result

    """

    # make linear regression
    slope, intercept, r_value, p_value, std_err = linregress(
        xdata, ydata)
    # plot it
    fig, ax = plt.subplots()
    plt.scatter(xdata, ydata, marker='+', color="C0", label="Data")
    plt.plot(xdata, (intercept + xdata * slope), color="C1", label="Lin Reg")
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.show()

    return slope, intercept
