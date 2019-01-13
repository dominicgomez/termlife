#!/usr/bin/env python3
# vim: set fileencoding=utf-8:


import unittest

from grid import Grid


class GridTestCase(unittest.TestCase):
    def setUp(self):
        self.g0 = Grid([])
        self.g1 = Grid([(7, 1), (9, 7), (9, 8), (9, 9)])
        self.g2 = Grid(
            [(-6, -8), (-6, -9), (-7, -9), (-8, -4), (-9, -3), (-9, -4)]
        )
        self.g3 = Grid(
            [(2, 6), (2, 7), (2, 8), (3, 6), (4, 4), (4, 7), (5, 3), (5, 4)]
        )

    def test_tick(self):
        self._test_tick(self.g0, [])
        self._test_tick(self.g1, [(8, 8), (9, 8), (10, 8)])
        self._test_tick(
            self.g2,
            [(-7, -9), (-6, -9), (-6, -8), (-7, -8), (-9, -4), (-9, -3),
             (-8, -4), (-8, -3)]
        )
        self._test_tick(
            self.g3,
            [(1, 7), (2, 6), (2, 7), (3, 5), (3, 6), (3, 8), (4, 3), (4, 4),
             (4, 5), (5, 3), (5, 4)]
        )

    def test_count_live_cells(self):
        self._test_count_live_cells(self.g0, [(4, 4), (-2, 3)], 0)
        self._test_count_live_cells(self.g1, [(9, 7), (10, 8)], 1)
        self._test_count_live_cells(self.g2, [(-6, -8), (-9, -3)], 2)
        self._test_count_live_cells(self.g3, [(2, 6), (0, 1)], 1)

    def test_get_neighbors(self):
        self._test_get_neighbors(
            (0, 0),
            {(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0),
             (1, 1)}
        )
        self._test_get_neighbors(
            (7, 1),
            {(6, 0), (6, 1), (6, 2), (7, 0), (7, 2), (8, 0), (8, 1), (8, 2)}
        )

    def _test_tick(self, g, nextgen):
        g.tick()
        self.assertEqual(g, Grid(nextgen))

    def _test_count_live_cells(self, g, cells, live_cells):
        self.assertEqual(g.count_live_cells(cells), live_cells)

    def _test_get_neighbors(self, cell, neighbors):
        self.assertEqual(Grid.get_neighbors(cell), neighbors)


if __name__ == '__main__':
    unittest.main()
