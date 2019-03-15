from abc import ABC, abstractmethod
from datetime import datetime


class _Layout(ABC):
    def __init__(self):
        ABC.__init__()


class FlowLayout(_Layout):
    def __init__(self):
        _Layout.__init__()


class GridLayout(_Layout):
    def __init__(self, rows, cols, ypad=0, xpad=0, sel=(0, 0)):
        _Layout.__init__()
        self.rows = rows
        self.cols = cols
        self.ypad = ypad
        self.xpad = xpad


class BarLayout(GridLayout):
    def __init__(self, pad):
        GridLayout.__init__(1, 0, xpad=pad)


class ListLayout(GridLayout):
    def __init__(self, pad):
        GridLayout.__init__(0, 1, ypad=pad)


class _Widget(ABC):
    """A base class for widgets."""
    def __init__(
        self, parent,
        height=None, width=None,
        ypad=0, xpad=0,
        anchor='topleft',
        img=None, bg=None, fg=None,
        layout=None, pos=None, justify='left',
        sel=False, action=None,
        cursor=False, visible=True,
        **opts
    ):
        ABC.__init__()

        self.BIRTH = datetime.now()
        self.PARENT = parent
        self.__dict__.update(opts)

    @abstractmethod
    def on_event(self, key):
        """Process user input."""
        pass

    @abstractmethod
    def update(self, **opts):
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

    def _justify(self, fmt):
        if fmt == 'left':
            pass
        elif fmt == 'right':
            pass
        elif fmt == 'center':
            pass
        elif fmt == 'full':
            pass
        else:
            pass

    def _anchor(self, pos):
        if pos == 'topleft':
            pass
        elif pos == 'top':
            pass
        elif pos == 'topright':
            pass
        elif pos == 'left':
            pass
        elif pos == 'center':
            pass
        elif pos == 'right':
            pass
        elif pos == 'bottomleft':
            pass
        elif pos == 'bottom':
            pass
        elif pos == 'bottomright':
            pass
        else:
            pass

    def _isoffscreen(self, par_h, par_w):
        # Determine whether any part of the widget lies off-screen.
        y, x = self.pos
        return (y+self.h >= par_h) or (x+self.w >= par_w)


class _WidgetGroup(ABC):
    def __init__(self, grp):
        ABC.__init__()
        self.grp = grp

    @abstractmethod
    def onevent(self, k):
        pass

    @abstractmethod
    def update(self, **opts):
        pass

    @abstractmethod
    def render(self):
        pass


class RadioButtonGroup(_WidgetGroup):
    def __init__(self, rbs):
        _WidgetGroup.__init__(rbs)

    def onevent(self, k):
        pass

    def update(self, **opts):
        pass

    def render(self):
        pass
