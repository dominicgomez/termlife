#!/usr/bin/env python3
# vim: set fileencoding=utf-8:


def tick(grid):
    """Compute the next generation of the universe.

    Live cells with fewer than two or more than three live neighbors die, and
    live cells with two or three live neighbors survive.

    Dead cells with exactly three live neighbors become live.

    Parameters
    ----------
    grid : set of tuple of int
        A unique, unordered collection of the row and column coordinates of the
        live cells in the universe.

    Returns
    -------
    set of tuple of int
        A unique, unordered collections of the row and column coordinates of
        the live cells in the newly computed generation.

    """
    _grid = set()
    watch = set()
    for live_cell in grid:
        ns = neighbors(live_cell)
        watch = watch.union({n for n in ns if n not in grid})
        if population(grid, ns) == 2 or population(grid, ns) == 3:
            _grid.add(live_cell)
    for dead_cell in watch:
        ns = neighbors(dead_cell)
        if population(grid, ns) == 3:
            _grid.add(dead_cell)
    return _grid


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

    """
    return sum([1 for c in cells if c in grid])


if __name__ == '__main__':
    pass
