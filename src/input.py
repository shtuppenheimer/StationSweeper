# src/input.py
import curses

def handle_input(key, player, grid):
    if key == curses.KEY_UP:
        player.move(0, -1, grid)
    elif key == curses.KEY_DOWN:
        player.move(0, 1, grid)
    elif key == curses.KEY_LEFT:
        player.move(-1, 0, grid)
    elif key == curses.KEY_RIGHT:
        player.move(1, 0, grid)
