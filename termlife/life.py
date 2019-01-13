def tick(grid):
    """Compute the next generation of cells.

    Parameters
    ----------
    grid : set of tuple of int
        A collection of the live cells in the grid.

    Returns
    -------
    set of tuple of int
        The new generation of cells.

    """

    # The new grid.
    grid_ = set()
    # The grid is infinite, so we can't count every cell's neighbors. Instead,
    # keep a collection of dead cells that have live neighbors. Apart from each
    # of the live cells in the grid, these dead cells are the only other cells
    # of interest.
    watch = set()

    for lcell in grid:
        # Live cells with fewer than two live neighbors or more than three live
        # neighbors die, and live cells with two or three live neighbors
        # survive.
        lcells = _numlive(grid, _nbors(lcell))
        if lcells == 2 or lcells == 3:
            grid_.add(lcell)

        watch = watch.union({n for n in _nbors(lcell) if n not in grid})

    for dcell in watch:
        # Dead cells with exactly three live neighbors become live.
        if _numlive(grid, _nbors(dcell)) == 3:
            grid_.add(dcell)

    return grid_


def _nbors(cell):
    # Get a cell's eight neighbors.
    r, c = cell
    return [
        (r-1, c-1),     # NW
        (r-1, c),       # N
        (r-1, c+1),     # NE
        (r, c-1),       # W
        (r, c+1),       # E
        (r+1, c-1),     # SW
        (r+1, c),       # S
        (r+1, c+1)      # SE
    ]


def _numlive(grid, cells):
    # Count the live cells in `cells`.
    return sum([1 for c in cells if c in grid])
