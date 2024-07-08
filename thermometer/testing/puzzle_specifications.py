"""A module hosting various Thermometer Puzzle specifications, organised by puzzle IDs.
"""

import numpy as np

# TODO: Add examples of a 4x4 & 6x6 straight puzzle and straight/curved 10x10 & 15x15 examples.
# A dictionary of testing data hosting various puzzle specifications corresponding to Thermometer Puzzle IDs.
thermometer_puzzle_specifications = {
    # A sample ID of a 4x4 Curved Thermometer Puzzle & it's corresponding data representation.
    366_983: {
        "thermometer_grid": np.array(
            [
                [[0, 0, 1, 1], [2, 2, 1, 1], [3, 3, 3, 3], [4, 4, 4, 3]],
                [[0, 1, 3, 2], [0, 1, 0, 1], [0, 1, 2, 3], [0, 1, 2, 4]],
            ]
        ),
        "row_constraints": [1, 2, 2, 2],
        "column_constraints": [2, 2, 1, 2],
    },
    # A sample ID of a 6x6 Curved Thermometer Puzzle & it's corresponding data representation.
    9_682_815: {
        "thermometer_grid": np.array(
            [
                [
                    [0, 0, 0, 0, 0, 0],
                    [0, 1, 1, 2, 2, 0],
                    [3, 3, 4, 4, 5, 0],
                    [3, 3, 6, 6, 5, 5],
                    [7, 7, 6, 6, 5, 5],
                    [7, 7, 8, 8, 8, 8],
                ],
                [
                    [7, 6, 5, 4, 3, 2],
                    [8, 1, 0, 1, 0, 1],
                    [0, 3, 1, 0, 0, 0],
                    [1, 2, 1, 0, 1, 4],
                    [1, 0, 2, 3, 2, 3],
                    [2, 3, 3, 2, 1, 0],
                ],
            ]
        ),
        "row_constraints": [4, 1, 4, 4, 2, 2],
        "column_constraints": [4, 1, 2, 3, 3, 4],
    },
}
