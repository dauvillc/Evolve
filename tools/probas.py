"""
Defines density laws or discrete probabilities used by the simulation.
"""
import numpy as np
import numpy.random as rd


def centered_geometric(p, n=1, size=1):
    """
    Returns a sample from the geometric law of parameter p, whose
    variance has been reduced by taking the mean of n experiences.
    The std of the returned sample is s/sqrt(n) where s is the original
    std, i.e. s = sqrt(p(1-p)).
    """
    if isinstance(size, int):
        size = [size]
    size = [n] + list(size)
    return np.sum(rd.geometric(p, size), axis=0) / n
