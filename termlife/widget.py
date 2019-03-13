"""Widgets for curses interfaces.

THIS CLASS CANNOT BE INSTANTIATED. It only outlines and documents the
components necessary to derive an instantiable widget class.

"""
from abc import ABC, abstractmethod

import util


class Widget(ABC):
    """A GUI-like component for curses interfaces.

    Parameters
    ----------
    parent: Window
        The window on which to display the widget.
        These are the window objects returned by ``curses.initscr()``,
        ``curses.newwin()``, etc.
    img: str
        An image of the widget in ASCII art.
    pos: tuple(int, int)
        The initial coordinates of the top-left corner of the widget on its
        parent window.

    Attributes
    ----------
    parent: Window
        The window on which to display the widget.
        These are the window objects returned by ``curses.initscr()``,
        ``curses.newwin()``, etc.
    img: str
        An image of the widget in ASCII art.
    pos: tuple(int, int)
        The initial coordinates of the top-left corner of the widget on its
        parent window.
    win: Window
        The window (in the parent window) on which the widget is drawn.
    visible: bool
        Whether the widget is visible.

    """
    @abstractmethod
    def __init__(self, parent, img, pos):
        self.parent = parent
        self.img = img
        self.h, self.w = self._get_sz()
        self.pos = self._set_pos(pos)
        # Writing to the last column of the last line of the terminal causes
        # the cursor to advance off screen, resulting in error. To avoid this,
        # the label window is 1 row of terminal cells taller than the widget it
        # displays.
        self.win = self.parent.derwin(self.h+1, self.w, *self.pos)
        self.visible = True

    @abstractmethod
    def on_input(self, key):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def _get_sz(self):
        pass

    def _set_pos(self, pos):
        if isinstance(pos, str):
            parent_h, parent_w = self.parent.getmaxyx()
            if pos == 'center':
                return util.center(parent_h, parent_w, self.h, self.w)
            elif pos == 'topcenter':
                return (0, util.center_x(parent_w, self.w))
            else:
                pass
        elif isinstance(pos, tuple):
            return tuple
        else:
            pass
