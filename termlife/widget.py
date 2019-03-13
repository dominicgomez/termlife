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
        The ascii art representing the widget.
    pos: str or tuple(int, int), optional(default=(0, 0))
        The (y, x) coordinates of the widget's top-left corner relative to its
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
        The coordinates of the top-left corner of the widget on its parent
        window.
    win: Window
        The window (in the parent window) on which the widget is drawn.
    visible: bool
        Whether the widget is visible.

    """
    @abstractmethod
    def __init__(self, parent, img, pos=(0, 0)):
        self.parent = parent
        self.img = img
        self.height = len(self.img.split('\n'))
        self.width = max(len(line) for line in self.img.split('\n'))
        self.pos = self._pos(pos)
        # Typing on the last column of the last line of the terminal causes the
        # cursor to advance off screen, resulting in error. To avoid this, the
        # label window is 1 row of terminal cells taller than the widget it
        # displays.
        self.win = self.parent.derwin(self.height+1, self.width, *self.pos)
        self.visible = True

    @abstractmethod
    def oninput(self, key):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def render(self):
        pass

    def _pos(self, pos):
        if isinstance(pos, str):
            if pos == 'center':
                return self._center()
            elif pos == 'topcenter':
                return (0, self._xcenter())
            else:
                pass
        elif isinstance(pos, tuple):
            return tuple
        else:
            pass

    def _center(self):
        return (self._ycenter(), self._xcenter())

    def _ycenter(self):
        parent_height, _ = self.parent.getmaxyx()
        return (parent_height-self.height)//2

    def _xcenter(self):
        _, parent_width = self.parent.getmaxyx()
        return (parent_width-self.width)//2
