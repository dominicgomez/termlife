import widget


class Label((widget.Widget)):
    def __init__(self, parent, img, pos=None):
        super().__init__(parent, img, pos)

    def oninput(self, key):
        pass

    def update(self):
        pass
