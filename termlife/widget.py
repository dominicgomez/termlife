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
    height: int
        The height of the widget.
    width: int
        The width of the widget.
    pos: tuple(int, int)
        The coordinates of the top-left corner of the widget on its parent
        window.
    win: Window
        The window (in the parent window) on which the widget is drawn.
    visible: bool
        Whether the widget is visible.

    """
    @abstractmethod
    def __init__(self, parent, img, pos=None):
        self.parent = parent
        self.img = img.split('\n')
        self.height = len(self.img)
        self.width = max(len(line) for line in self.img)
        self.pos = self._setpos(pos)
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

    def _setpos(self, pos):
        if isinstance(pos, str):
            if pos == 'center':
                return self._center()
            else:
                pass
        elif isinstance(pos, tuple):
            return pos
        else:
            return (0, 0)

    def _center(self):
        return (self._centery(), self._centerx())

    def _centery(self):
        return (self.parent.getmaxyx()[0]-self.height)//2

    def _centerx(self):
        return (self.parent.getmaxyx()[1]-self.width)//2
