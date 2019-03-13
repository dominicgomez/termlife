#!/usr/bin/env python3
# vim: set fileencoding=utf-8:

import curses

import widgets


def main(stdscr):
    stdscr.clear()

    testlabel = widgets.Label(stdscr, 'Dominic Gomez')
    testlabel.render()

    stdscr.getkey()
    testlabel.visible = False
    testlabel.render()

    stdscr.getkey()
    testlabel.visible = True
    testlabel.render()

    stdscr.getkey()

    stdscr.refresh()


if __name__ == '__main__':
    curses.wrapper(main)
