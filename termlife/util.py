import math


def center(target_h, target_w, src_h, src_w):
    return (center_y(target_h, src_h), center_x(target_w, src_w))


def center_y(target_h, src_h):
    return math.floor((target_h-src_h)/2)


def center_x(target_w, src_w):
    return math.floor((target_w-src_w)/2)
