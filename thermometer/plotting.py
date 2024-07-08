"""A module for providing plots/visualisations of the input data and solution
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap


def plot_puzzle(
    thermometer_grid: np.ndarray,
    row_constraints: np.ndarray,
    column_constraints: np.ndarray,
) -> None:
    """Plots a visualisation of the thermometer puzzle from its input
    data specification.

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
    """
    # Generate a random colormap to visualise unique thermometers.
    random_colormap = ListedColormap(colors=np.random.rand(256, 3))

    # Instantiate an axis to form the basis of the plot.
    _, ax = plt.subplots()

    # Extract the thermometer ids from the grid specification.
    thermometer_ids = np.unique(thermometer_grid[0, ...])

    # Iterate over each thermometer.
    for id_ in thermometer_ids:
        # Extract the cell indices that the thermometer in consideration spans.
        thermometer_cells = np.argwhere(thermometer_grid[0, ...] == id_)

        # Get the ordered indices of the cells for the thermometer in consideration.
        thermometer_cell_ordered_indices = np.argsort(
            thermometer_grid[-1, ...][thermometer_cells[:, 0], thermometer_cells[:, 1]]
        )

        # Extract the indices of the thermometer cells specified in sequential order.
        thermometer_sequence_indices = np.stack(
            (
                thermometer_cell_ordered_indices[:-1],
                thermometer_cell_ordered_indices[1:],
            ),
            axis=-1,
        )

        # Iterate over each pair of thermometer cells that occur in sequence.
        for vector_start, vector_end in thermometer_cells[thermometer_sequence_indices]:
            # Plot a vector between the starting and ending cells.
            ax.quiver(
                vector_start[1],
                vector_start[0],
                vector_end[1] - vector_start[1],
                vector_end[0] - vector_start[0],
                angles="xy",
                scale_units="xy",
                scale=1,
                color="black",
            )

    # Display the thermometer grid array, colored by each thermometer class.
    ax.imshow(thermometer_grid[0, ...], cmap=random_colormap)

    # Specify the underlying grid to attach to the plot.
    ax.grid(True, which="both")
    ax.set_xticks(np.arange(-0.5, thermometer_grid.shape[2]), minor=True)
    ax.set_yticks(np.arange(-0.5, thermometer_grid.shape[1]), minor=True)
    ax.grid(which="minor", color="black", linestyle="-", linewidth=1)
    ax.grid(which="major", color="k", linestyle="-", linewidth=0)
    ax.set_axisbelow(True)

    # Specify the axes ticks and labels.
    ax.set_xticks(np.arange(thermometer_grid.shape[2]), minor=False)
    ax.set_yticks(np.arange(thermometer_grid.shape[1]), minor=False)
    ax.set_xticklabels(column_constraints)
    ax.set_yticklabels(row_constraints)
    ax.xaxis.tick_top()

    # Display the plot.
    plt.show()

    return


# TODO: Make this when done with the solver.
def plot_puzzle_solution(puzzle_solution: np.ndarray) -> None:
    """Plots a visualisation of the completed puzzle solution.

    :param puzzle_solution: A (M, N) boolean NumPy array
    representation of the puzzle solution. Here M is the
    number of puzzle rows and N is the number of puzzle
    columns.
    """
    # ...
    plt.imshow(puzzle_solution)

    return


if __name__ == "__main__":
    from testing.puzzle_specifications import thermometer_puzzle_specifications

    # Choose a sample Thermometer Puzzle ID from the test data.
    PUZZLE_ID = 9_682_815

    # Plot a representation of a puzzle for a specified puzzle ID.
    plot_puzzle(**thermometer_puzzle_specifications[PUZZLE_ID])
