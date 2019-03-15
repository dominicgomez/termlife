"""GUI-like components for curses interfaces."""
# import curses

from _widget import _Widget


class Frame(_Widget):
    """A rectangular region of the screen.

    Attributes
    ----------

    """
    def __init__(self, parent, **opts):
        self.parent = parent
        self.height = opts['height'] or self.parent.getmaxyx()[0]
        self.width = opts['width'] or self.parent.getmaxyx()[1]


class DialogBox(Frame):
    """Display multiple lines of text.

    Attributes
    ----------

    """
    def __init__(self, parent, **opts):
        pass


class MessageBox(DialogBox):
    def __init__(self, parent, **opts):
        pass


class Grid(_Widget):
    """Display multiple lines of text.

    Attributes
    ----------

    """
    def __init__(self, parent, **opts):
        pass


class List(Grid):
    """Display multiple lines of text.

    Attributes
    ----------

    """
    def __init__(self, parent, **opts):
        pass


class Menu(List):
    """Display multiple lines of text.

    Attributes
    ----------

    """
    def __init__(self, parent, **opts):
        pass


class TextBox(_Widget):
    """Display multiple lines of text.

    Attributes
    ----------

    """
    def __init__(self, parent, **opts):
        pass


class TextLabel(TextBox):
    """Display one line of text.

    Attributes
    ----------

    """
    def __init__(self, parent, **opts):
        pass


class ListItem(TextLabel):
    """Display multiple lines of text.

    Attributes
    ----------

    """
    def __init__(self, parent, **opts):
        pass


class ButtonGroup(_Widget):
    """Display multiple lines of text.

    Attributes
    ----------

    """
    def __init__(self, parent, **opts):
        pass


class RadioButtonGroup(ButtonGroup):
    """Display multiple lines of text.

    Attributes
    ----------

    """
    def __init__(self, parent, **opts):
        pass


class Button(_Widget):
    """Display multiple lines of text.

    Attributes
    ----------

    """
    def __init__(self, parent, **opts):
        self.action = opts['action']


class CheckBox(Button):
    """Display multiple lines of text.

    Attributes
    ----------

    """
    def __init__(self, parent, **opts):
        pass


class RadioButton(Button):
    """Display multiple lines of text.

    Attributes
    ----------

    """
    def __init__(self, parent, **opts):
        pass


# class Menu(List):
#     def __init__(self, parent, **opts):
#         pass

#     def on_input(self, key):
#         pass

#     def update(self):
#         pass

#     def render(self):
#         if self.visible:
#             self.win.addstr(*self.pos, self.img)

#     def _img(self, options, selector, selected, align):
#         return '+-----+\n|     |\n+-----+'


# class Label(_Widget):
#     # def __init__(self, parent, **opts):
#     #     pass

#     def __init__(self, parentent, text, pos, visible=True):
#         super(Label, self).__init__(parentent, text, pos, visible)

#     def on_input(self, key):
#         pass

#     def update(self):
#         pass

#     def render(self):
#         if self.visible:
#             self.win.addstr(*self.pos, self.img)
#         else:
#             self.win.erase()

#         self.win.refresh()
