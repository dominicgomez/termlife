#!/usr/bin/env python3
# vim: set fileencoding=utf-8:


def neighbors(cell):
    """Get a cell's neighbors.

    Every cell has exactly eight neighbors, which are the cells horizontally,
    vertically, and diagonally agjacent to it.

    Parameters
    ----------
    cell : tuple of int
        The row and column coordinates of the cell on the grid.

    Returns
    -------
    list of tuple of int
        The row and column coordinates of `cell`'s eight neighbors.

    Examples
    --------
    >>> neighbors((2, 5))
    [(1, 4), (1, 5), (1, 6), (2, 4), (2, 6), (3, 4), (3, 5), (3, 6)]

    >>> neighbors((-1, 2))
    [(-2, 1), (-2, 2), (-2, 3), (-1, 1), (-1, 3), (0, 1), (0, 2), (0, 3)]

    """
    row, col = cell
    return [
        (row+row_offset, col+col_offset)
        for row_offset in range(-1, 2) for col_offset in range(-1, 2)
        if (row_offset, col_offset) != (0, 0)
    ]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
