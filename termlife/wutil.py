"""Utilities for widgets."""
from enum import Enum


class Alignment(Enum):
    TOPLEFT = 0
    TOP = 1
    TOPRIGHT = 2
    LEFT = 3
    CENTER = 4
    RIGHT = 5
    BOTTOMLEFT = 6
    BOTTOM = 7
    BOTTOMRIGHT = 8


def align(widg, win, alignment):
    """TODO

    Parameters
    ----------
    w: widget.Widget
    win: Window
    alignment: wutil.Alignment

    """
    par_h, par_w = win.parent.getmaxyx()
    if alignment == Alignment.TOPLEFT:
        return (0, center(par_h, widg.h))
    elif alignment == Alignment.TOP:
        return (0, center(par_w, widg.w))
    elif alignment == Alignment.TOPRIGHT:
        return (0, par_w-widg.w)
    elif alignment == Alignment.LEFT:
        pass
    elif alignment == Alignment.CENTER:
        pass
    elif alignment == Alignment.RIGHT:
        pass
    elif alignment == Alignment.BOTTOMLEFT:
        pass
    elif alignment == Alignment.BOTTOM:
        pass
    elif alignment == Alignment.BOTTOMRIGHT:
        pass


def center(target, src):
    """TODO

    Parameters
    ----------
    target: int
        TODO
    src: int
        TODO

    """
    return (target-src)//2
