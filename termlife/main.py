#!/usr/bin/env python3
# vim: set fileencoding=utf-8:

from grid import Grid


def main(seed):
    g = Grid(seed)
    print(g)
    g.tick()
    print(g)


if __name__ == '__main__':
    main([(1, 3), (2, 4), (3, 2), (3, 3), (3, 4)])
