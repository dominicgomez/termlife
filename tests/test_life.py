import unittest

from termlife import life


class LifeTestCase(unittest.TestCase):
    def test_tick(self):
        seed = set()
        nextgen = set()
        self.assertEqual(life.tick(seed), nextgen)

        seed = set([(7, 1), (9, 7), (9, 8), (9, 9)])
        nextgen = set([(8, 8), (9, 8), (10, 8)])
        self.assertEqual(life.tick(seed), nextgen)

        seed = set(
            [(-6, -8), (-6, -9), (-7, -9), (-8, -4), (-9, -3), (-9, -4)]
        )
        nextgen = set(
            [(-7, -9), (-6, -9), (-6, -8), (-7, -8), (-9, -4), (-9, -3),
             (-8, -4), (-8, -3)]
        )
        self.assertEqual(life.tick(seed), nextgen)

        seed = set(
            [(2, 6), (2, 7), (2, 8), (3, 6), (4, 4), (4, 7), (5, 3), (5, 4)]
        )
        nextgen = set(
            [(1, 7), (2, 6), (2, 7), (3, 5), (3, 6), (3, 8), (4, 3), (4, 4),
             (4, 5), (5, 3), (5, 4)]
        )
        self.assertEqual(life.tick(seed), nextgen)


if __name__ == '__main__':
    unittest.main()
