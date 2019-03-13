import abc
import re


class Widget((abc.ABC)):
    """A GUI-like component for curses programs.

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
    cover: str
        `img`
    pos: tuple(int, int)
        The (y, x) coordinates of the widget's top-left corner relative to its
        parent window.
    win: Window
        The
    visible: bool
        Whether the widget is visible.

    """
    @abc.abstractmethod
    def __init__(self, parent, img, pos=None):
        self.parent = parent
        self.img = [line for line in img.split('\n') if line.strip()]
        self.cover = [re.sub(r'\S', ' ', line) for line in self.img]
        self.height, self.width = self.getsize()
        self.pos = self.setpos(pos)
        # Typing on the last column of the last line of the terminal causes the
        # cursor to advance off screen, resulting in error. To avoid this, the
        # label window is 1 row of terminal cells taller than the widget it
        # displays.
        self.win = self.parent.derwin(self.height+1, self.width, *self.pos)
        self.visible = True

    def align(self, alignment):
        if alignment == 'centertop':
            return (0, self.centerx())
        elif alignment == 'centerleft':
            return (self.centery(), 0)
        elif alignment == 'center':
            return self.center()
        elif alignment == 'centerright':
            _, pwidth = self.parent.getmaxyx()
            return (self.centery(), pwidth-self.width)
        elif alignment == 'centerbottom':
            pheight, _ = self.parent.getmaxyx()
            return (pheight-self.height, self.centerx())
        else:
            pass

    def center(self):
        return (self.centery(), self.centerx())

    def centery(self):
        pheight, _ = self.parent.getmaxyx()
        return (pheight-self.height)//2

    def centerx(self):
        _, pwidth = self.parent.getmaxyx()
        return (pwidth-self.width)//2

    def getsize(self):
        return (len(self.img), max(len(line) for line in self.img))

    def hide(self):
        self.visible = False

    @abc.abstractmethod
    def oninput(self, key):
        pass

    def render(self):
        img = self.img if self.visible else self.cover
        self.win.addstr(0, 0, '\n'.join(img))
        self.win.refresh()

    def setpos(self, pos):
        if isinstance(pos, str):
            return self.align(pos)
        elif isinstance(pos, tuple):
            return pos
        else:
            return (0, 0)

    def unhide(self):
        self.visible = True

    @abc.abstractmethod
    def update(self):
        pass
