#!/usr/bin/env python3
# vim: set fileencoding=utf-8:

import curses

import widgets


def main(stdscr):
    stdscr.clear()

    testlabel = widgets.Label(stdscr, 'Dominic Gomez', 'center')
    testlabel.render()

    stdscr.getkey()
    testlabel.hide()
    testlabel.render()

    stdscr.getkey()
    testlabel.unhide()
    testlabel.render()

    stdscr.getkey()

    stdscr.refresh()


if __name__ == '__main__':
    curses.wrapper(main)
