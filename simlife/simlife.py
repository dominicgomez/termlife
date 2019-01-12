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
    iterable of tuple of int
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


def population(grid, cells):
    """Count the live cells.

    Parameters
    ----------
    grid : set of tuple of int
        A unique, unordered collection of the row and column coordinates of the
        live cells in the universe.
    cells : iterable of tuple of int
        The row and column coordinates of the cells to test.

    Returns
    -------
    int
        The number of live cells in `cells`.

    Examples
    --------
    >>> g = {(1, 3), (2, 4), (3, 2), (3, 3), (3, 4)}

    >>> cs1 = [(1, 2), (1, 3), (1, 4), (2, 2), (2, 4), (3, 2), (3, 3), (3, 4)]

    >>> cs2 = [(-1, 0), (0, 0), (1, 0)]

    >>> population(g, cs1)
    5

    >>> population(g, cs2)
    0

    """
    return sum([1 for c in cells if c in grid])


if __name__ == '__main__':
    import doctest
    doctest.testmod()
