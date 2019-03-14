"""GUI-like components for curses interfaces."""
# import curses

from widget import Widget


class Grid(Widget):
    def __init__(self, parent, rows, cols, pos, visible=True):
        pass

    def on_input(self, key):
        pass

    def update(self):
        pass

    def render(self):
        pass


class Label(Widget):
    def __init__(self, parent, text, pos, visible=True):
        # `_height` and `_width` must be set before calling the parent class's
        # ``__init__`` method.
        super(Label, self).__init__(parent, text, pos, visible)

    def on_input(self, key):
        pass

    def update(self):
        pass

    def render(self):
        if self.visible:
            self.win.addstr(*self.pos, self.img)
        else:
            self.win.erase()

        self.win.refresh()


class Menu(Widget):
    def __init__(self, parent, img, pos, visible=True):
        pass

    def on_input(self, key):
        pass

    def update(self):
        pass

    def render(self):
        pass
