import datetime
import sys
from abc import ABC, abstractmethod


class Widget(ABC):
    """A base class for widgets.

    THIS CLASS CANNOT BE INSTANTIATED. All derived classes are required to
    implement its abstract methods.

    Parameters
    ----------
    parent: Window
        The window on which to place the widget's window.
    img: str
        An image of the widget in ASCII art.
    pos: tuple(int, int):
        The coordinates of the top-left corner of the widget.
    visible: bool
        Whether the widget is visible.

    Attributes
    ----------
    parent: Window
        The window on which to place the widget's window.
    img: str
        An image of the widget in ASCII art.
    h: int
        The widget's height.
    w: int
        The widget's width.
    pos: tuple(int, int):
        The coordinates of the top-left corner of the widget.
    visible: bool, optional(default=True)
        Whether the widget is visible.
    win: Window
        The window on which to display the widget.
    init_time: datetime.datetime
        The time that the widget was initialized. Could be useful for widgets
        that update after a certain amount of time (for flashing, for example).

    """
    def __init__(self, parent, img, pos, visible):
        self.parent = parent
        self.img = img

        par_h, par_w = self.parent.getmaxyx()
        self.h = len(self.img.split('\n'))
        if self.h >= par_h:
            sys.exit('widget too large for parent window')
        self.w = max(len(line) for line in self.img.split('\n'))
        if self.w >= par_w:
            sys.exit('widget too large for parent window')

        self.pos = pos
        if self._offscreen():
            sys.exit('widget positioned off-screen')

        self.visible = visible

        # Writing to the last column of the last line of a window causes the
        # cursor to advance off the window, resulting in error. To avoid this,
        # the widget window is 1 row taller than the widget it displays.
        self.win = self.parent.derwin(self.h+1, self.w, *self.pos)

        self.init_time = datetime.datetime.now()

    @abstractmethod
    def on_input(self, key):
        """Process user input."""
        pass

    @abstractmethod
    def update(self):
        """Update the widget."""
        pass

    @abstractmethod
    def render(self):
        """Draw the widget on the screen."""
        pass

    def hide(self):
        """Make the widget invisible."""
        if not self.visible:
            self.visible = False

    def unhide(self):
        """Make the widget visible."""
        if self.visible:
            self.visible = True

    def _offscreen(self):
        # Determine whether any part of the widget lies off-screen.
        y, x = self.pos
        par_h, par_w = self.parent.getmaxyx()
        return (y+self.h >= par_h) or (x+self.w >= par_w)
