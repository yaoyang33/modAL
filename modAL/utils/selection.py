"""
Functions to select certain element indices from arrays.
"""

import numpy as np


def multi_argmax(values, n_instances=1):
    """
    Selects the indices of the n_instances highest values.

    :param values:
        Contains the values to be selected from.
    :type values:
        numpy.ndarray of shape = (n_samples, 1)

    :param n_instances:
        Specifies how many indices to return.
    :type n_instances:
        int

    :returns:
      - **max_idx** *(numpy.ndarray of shape = (n_samples, 1))* --
        Contains the indices of the n_instances largest values.

    """
    assert n_instances <= len(values), 'n_instances must be less or equal than the size of utility'

    max_idx = np.argpartition(-values, n_instances-1, axis=0)[:n_instances]
    return max_idx


def weighted_random(weights, n_instances=1):
    """
    Returns n_instances indices based on the weights.

    :param weights:
        Contains the weights of the sampling.
    :type weights:
        numpy.ndarray of shape = (n_samples, 1)

    :param n_instances:
        Specifies how many indices to return.
    :type n_instances:
        int

    :returns:
      - **random_idx** *(numpy.ndarray of shape = (n_instances, 1))* --
        n_instances random indices based on the weights.
    """
    assert n_instances <= len(weights), 'n_instances must be less or equal than the size of utility'
    weight_sum = np.sum(weights)
    assert weight_sum > 0, 'the sum of weights must be larger than zero'

    random_idx = np.random.choice(range(len(weights)), size=n_instances, p=weights/weight_sum, replace=False)
    return random_idx
