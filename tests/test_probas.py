import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
from tools.probas import centered_geometric


if __name__ == "__main__":
    # Computes samples from the centered geometric law
    # With variance reductors of 1 (base), 10 and 100
    X = range(30)
    base = [centered_geometric(0.1) for _ in X]
    centered_10 = [centered_geometric(0.1, 10) for _ in X]
    centered_100 = [centered_geometric(0.1, 100) for _ in X]

    # Applies the gaussian kernel density estimation
    # rather than plotting the histogram
    bandwith = 5.0
    values = np.linspace(0, 30, 100)
    density_base = []
    density_10 = []
    density_100 = []
    for value in values:
        count = 0
        for y in base:
            if value - bandwith / 2 <= y < value + bandwith / 2:
                count += stats.norm.pdf(y - value)[0]
        density_base.append(count)
        for y in centered_10:
            if value - bandwith / 2 <= y < value + bandwith / 2:
                count += stats.norm.pdf(y - value)[0]
        density_10.append(count)
        for y in centered_100:
            if value - bandwith / 2 <= y < value + bandwith / 2:
                count += stats.norm.pdf(y - value)[0]
        density_100.append(count)

    # Plots the densities obtained
    # to check that their mean is actually 10 and
    # to have a look at the variance
    plt.plot(values, density_base, "g-")
    plt.plot(values, density_10, "b-")
    plt.plot(values, density_100, "y-")
    plt.legend(["Base", "Centered 10", "Centered 100"])
    plt.show()