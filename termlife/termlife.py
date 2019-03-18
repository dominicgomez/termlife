import curses
from math import floor


HLINE = u'\u2500'       # ─
VLINE = u'\u2502'       # │
TOPLEFT = u'\u250C'     # ┌
LEFT = u'\u251C'        # ├
BOTLEFT = u'\u2514'     # └
TOP = u'\u252C'         # ┬
XLINE = u'\u253C'       # ┼
BOT = u'\u2534'         # ┴
TOPRIGHT = u'\u2510'    # ┐
RIGHT = u'\u2524'       # ┤
BOTRIGHT = u'\u2518'    # ┘

DEAD = ' '
ALIVE = u'\u2588'       # █
CURSOR = u'\u2591'      # ░


def get_grid_size(win):
    h, w = win.getmaxyx()
    return (floor((h-1)/2), floor((w-1)/2))


def get_grid_img(rows, cols):
    top = TOPLEFT+(TOP.join([HLINE]*cols))+TOPRIGHT
    mid_h = LEFT+(XLINE.join([HLINE]*cols))+RIGHT
    mid_v = VLINE+(VLINE.join(' '*cols))+VLINE
    bot = BOTLEFT+(BOT.join([HLINE]*cols))+BOTRIGHT

    return top+(mid_h.join(['\n'+mid_v+'\n']*rows))+bot


def to_term_pos(grid_row, grid_col):
    return (2*grid_row+1, 2*grid_col+1)


def main():
    stdscr = curses.initscr()
    prep_term(stdscr)
    term_h, term_w = stdscr.getmaxyx()

    grid_win = stdscr.derwin(term_h-1, term_w, 0, 0)
    grid_row, grid_col = (0, 0)
    grid_rows, grid_cols = get_grid_size(grid_win)
    grid_img = get_grid_img(grid_rows, grid_cols)

    render_grid(grid_win, grid_img, grid_row, grid_col)

    cmd_win = stdscr.derwin(1, term_w, term_h-1, 0)

    key = None
    while key != ord('q'):

        cmd_win.erase()

        if key == ord(':'):
            cmd_win.addstr(0, 0, ':')
        elif key == ord('h'):
            if grid_col > 0:
                grid_col -= 1
            else:
                cmd_win.addstr(0, 0, 'WARNING')
        elif key == ord('j'):
            if grid_row < grid_rows-1:
                grid_row += 1
            else:
                cmd_win.addstr(0, 0, 'WARNING')
        elif key == ord('k'):
            if grid_row > 0:
                grid_row -= 1
            else:
                cmd_win.addstr(0, 0, 'WARNING')
        elif key == ord('l'):
            if grid_col < grid_cols-1:
                grid_col += 1
            else:
                cmd_win.addstr(0, 0, 'WARNING')
        elif key == ord('\n'):
            cmd_win.addstr(0, 0, 'ENTER PRESSED')

        grid_win.refresh()
        cmd_win.refresh()
        stdscr.refresh()

        key = stdscr.getch()

    reset_term(stdscr)


def prep_term(stdscr):
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)

    curses.curs_set(0)
    if curses.has_colors():
        curses.start_color()
        curses.use_default_colors()


def render_grid(win, img, cursor_row, cursor_col):
    win.addstr(0, 0, img)
    win.addstr(*to_term_pos(0, 0), CURSOR)


def reset_term(stdscr):
    stdscr.keypad(False)
    curses.nocbreak()
    curses.echo()
    curses.endwin()


if __name__ == '__main__':
    main()
