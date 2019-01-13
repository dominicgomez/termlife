__all__ = ['Grid']
__version__ = '1.0.0'
__author__ = 'Dominic Gomez'


class Grid:
    """The universe of the Game of Life.

    The universe of the Game of Life is an infinite, two-dimensional orthogonal
    grid of square cells, each of which may be either alive or dead.

    Parameters
    ----------
    seed : list of tuple of int
        The row and column coordinates of the initial collection of live cells
        in the universe (generation 0).

    Attributes
    ----------
    gens : list of set of tuple of int
        An ordered collection of unique, unordered collections of the row and
        column coordinates of the live cells in each generation of the
        universe. Indexed by the generation of the count_live_cells.

    """

    def __init__(self, seed):
        self.gens = [set(seed)]

    def __eq__(self, other):
        return self.gens[-1] == other.gens[-1]

    def __str__(self):
        return str(self.gens[-1])

    def tick(self):
        """Compute the next generation.

        Live cells with fewer than two or more than three live neighbors die,
        and live cells with two or three live neighbors survive. Dead cells
        with exactly three live neighbors become live.

        """
        grid = set()
        watch = set()
        for live_cell in self.gens[-1]:
            ns = self.get_neighbors(live_cell)
            watch = watch.union({n for n in ns if n not in self.gens[-1]})
            num_live_cells = self.count_live_cells(ns)
            if num_live_cells == 2 or num_live_cells == 3:
                grid.add(live_cell)
        for dead_cell in watch:
            ns = self.get_neighbors(dead_cell)
            if self.count_live_cells(ns) == 3:
                grid.add(dead_cell)
        self.gens.append(grid)

    def count_live_cells(self, cells):
        """Count the live cells.

        Parameters
        ----------
        cells : set of tuple of int
            The row and column coordinates of the cells to test.

        Returns
        -------
        int
            The number of live cells in `cells`.

        """
        return sum([1 for c in cells if c in self.gens[-1]])

    @staticmethod
    def get_neighbors(cell):
        """Get a cell's neighbors.

        Every cell has exactly eight neighbors, which are the cells
        horizontally, vertically, and diagonally adjacent to it.

        Parameters
        ----------
        cell : tuple of int
            The row and column coordinates of the cell.

        Returns
        -------
        set of tuple of int
            A unique, unordered collection of the row and column coordinates of
            `cell`'s eight neighbors.

        """
        row, col = cell
        return {
            (row+row_offset, col+col_offset)
            for row_offset in range(-1, 2) for col_offset in range(-1, 2)
            if (row_offset, col_offset) != (0, 0)
        }
