"""Widgets for curses interfaces.

THIS CLASS CANNOT BE INSTANTIATED. It only outlines and documents the
components necessary to derive an instantiable widget class.

"""
from abc import ABC, abstractmethod


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
    pos: tuple(int, int), optional(default=(0, 0))
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
    visible: bool
        Whether the widget is visible.

    """
    @abstractmethod
    def __init__(self, parent, img, pos=(0, 0)):
        self.parent = parent
        self.img = img
        self.pos = pos
        self.visible = True
        self._win = None
        # self.h, self.w = self._get_sz()
        # self.pos = self._set_pos(pos)
        # Writing to the last column of the last line of the terminal causes
        # the cursor to advance off screen, resulting in error. To avoid this,
        # the label window is 1 row of terminal cells taller than the widget it
        # displays.
        # self.win = self.parent.derwin(self.h+1, self.w, *self.pos)

    @abstractmethod
    def on_input(self, key):
        """Process user input."""
        pass

    @abstractmethod
    def update(self):
        """Update the widget's internal data."""
        pass

    @abstractmethod
    def render(self):
        """Draw the widget on the screen."""
        pass

    @property
    def win(self):
        try:
            return self._win
        except AttributeError:
            pass

    @win.setter
    def win(self, value):
        self._win = value
