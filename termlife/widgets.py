import widget


class Label((widget.Widget)):
    def __init__(self, parent, img, pos=None):
        super().__init__(parent, img, pos)

    def oninput(self, key):
        pass

    def update(self):
        pass

    def render(self):
        if self.visible:
            self.win.addstr(0, 0, '\n'.join(self.img))
        else:
            self.win.erase()

        self.win.refresh()
