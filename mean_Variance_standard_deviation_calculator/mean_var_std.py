"""
This module has one function named calculate() that uses Numpy
to output the mean, variance, standard deviation, max, min, and sum of
the rows, columns, and elements in a 3 x 3 matrix.

The input of the function is a list containing 9 digits.
The function converts the list into a 3 x 3 Numpy array,
and then returns a dictionary containing the mean, variance,
standard deviation, max, min, and sum along both axes and for the flattened matrix.
"""
from typing import Union
import numpy as np


def calculate(num_list: list) -> dict[str, list[list[Union[int, float]]]]:
    """Calculate the mean, variance, standard deviation, max, min and sum
    along both axes and for a flattened matrix.
    The input list must have 9 elements. Not more nor less.

    Args:
        num_list (list): Input list of numbers for the matrix.

    Raises:
        ValueError: Raise Value Error if the elements are not exactly 9 elements.

    Returns:
        dict[str, list[list[Union[int, float]]]]: Dictionary with all calculations.
    """

    if len(num_list) != 9:
        raise ValueError("List must contain nine numbers.")

    num_matrix: np.array = np.array(num_list).reshape((3, 3))

    calculations: dict[str, list[list[Union[int, float]]]] = {
        "mean": [
            np.mean(num_matrix, axis=0).tolist(),
            np.mean(num_matrix, axis=1).tolist(),
            np.mean(num_matrix.tolist()),
        ],
        "variance": [
            np.var(num_matrix, axis=0).tolist(),
            np.var(num_matrix, axis=1).tolist(),
            np.var(num_matrix.tolist()),
        ],
        "standard deviation": [
            np.std(num_matrix, axis=0).tolist(),
            np.std(num_matrix, axis=1).tolist(),
            np.std(num_matrix.tolist()),
        ],
        "max": [
            np.max(num_matrix, axis=0).tolist(),
            np.max(num_matrix, axis=1).tolist(),
            np.max(num_matrix.tolist()),
        ],
        "min": [
            np.min(num_matrix, axis=0).tolist(),
            np.min(num_matrix, axis=1).tolist(),
            np.min(num_matrix.tolist()),
        ],
        "sum": [
            np.sum(num_matrix, axis=0).tolist(),
            np.sum(num_matrix, axis=1).tolist(),
            np.sum(num_matrix).tolist(),
        ],
    }

    return calculations
