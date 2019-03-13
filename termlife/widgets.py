from widget import Widget


class Label(Widget):
    def __init__(self, parent, text, pos, visible=True):
        super(Label, self).__init__(parent, text, pos, visible)

    def on_input(self, key):
        pass

    def update(self):
        pass

    def render(self):
        if self.visible:
            self.win.addstr(0, 0, self.img)
        else:
            self.win.erase()

        self.win.refresh()

# class PlainText(ABC, Widget):
#     @abstractmethod
#     def __init__(self, parent, text, pos=None):
#         super().__init__()
#         super().__init__(parent, text, pos)

#     def oninput(self, key):
#         pass

#     def update(self):
#         pass

#     def render(self):
#         if self.visible:
#             self.win.addstr(0, 0, '\n'.join(self.img))
#         else:
#             self.win.erase()

#         self.win.refresh()


# class TextBlock(PlainText):
#     def __init__(self, parent, img, pos=None):
#         super().__init__(parent, img, pos)


# class Label(TextBlock):
#     def __init__(self, parent, img, pos=None):
#         super().__init__(parent, img, pos)
