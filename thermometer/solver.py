"""A module hosting the necessary functionality for creating a generic Thermometer Puzzle solver.
"""

import numpy as np


def solve(
    thermometer_grid: np.ndarray,
    row_constraints: np.ndarray,
    column_constraints: np.ndarray,
) -> np.ndarray:
    """Solves an arbitrary Thermometer Puzzle.

    :param thermometer_grid: The grid containing thermometer information.
     This information is represented by a (2, M, N) NumPy array, where M
     is the number of puzzle rows and N is the number of puzzle columns.
     In order, the first axis indexes: thermometer IDs & the distance of
     a cell away from its thermometer's base cell.
    :param row_constraints: The constraints for the rows of the puzzle grid.
     This information is represented by a (M,) NumPy array, where M is the number
     of grid rows. Here the element at index i represents the target thermometer
     sum for the i-th row.
    :param column_constraints: The constraints for the columns of the puzzle grid.
     This information is represented by a (N,) NumPy array, where N is the number
     of grid columns. Here the element at index j represents the target thermometer
     sum for the j-th column.
    :return: A (M, N) boolean NumPy array representation of the solution to the
     thermometer puzzle.
    """
    #

    #

    #

    return


#
if __name__ == "__main__":
    #
    pass
