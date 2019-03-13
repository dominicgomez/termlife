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
    pos: tuple(int, int) or str
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
    h: int
        The height of the widget.
    w: int
        The width of the widget.
    pos: tuple(int, int)
        The coordinates of the top-left corner of the widget on its parent
        window.
    win: Window

    visible: bool
        Whether the widget is visible.

    """
    # TOP_LEFT = 0
    # TOP_CENTER = 0
    # TOP_RIGHT = 0
    # CENTER_LEFT = 0
    # CENTER = 0
    # CENTER_RIGHT = 0
    # BOTTOM_LEFT = 0
    # BOTTOM_CENTER = 0
    # BOTTOM_RIGHT = 0

    @abstractmethod
    def __init__(self, parent, img, pos, visible=True):
        self.parent = parent
        self.img = img
        self.h = len(self.img.split('\n'))
        self.w = max(len(line) for line in self.img.split('\n'))
        self.ypos, self.xpos = pos
        self.win = self.parent.derwin(self.h+1, self.w, self.ypos, self.xpos)
        self.visible = visible
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
