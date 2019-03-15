from abc import ABC, abstractmethod


class _Scene(ABC):
    # A particular screen in the program.
    #
    # THIS CLASS CANNOT BE INSTANTIATED. All scenes derived from this abstract
    # base class are responsible for processing user input, updating internal
    # data, and drawing to the screen.
    def __init__(self):
        ABC.__init__()
        self.nxt = self

    @abstractmethod
    def on_event(self, key):
        # Process user input.
        pass

    @abstractmethod
    def update(self, **opts):
        # Update internal data.
        pass

    @abstractmethod
    def render(self):
        # Draw to the screen.
        pass

    def load(self, nxt):
        # Queue a scene to be loaded on the next frame.
        self.nxt = nxt

    def kill(self):
        # Terminate the program.
        self.load(None)
