# src/input.py
import curses




def handle_input(key, player, grid):
    dx, dy = 0, 0
    if key == curses.KEY_UP:
        dy = -1
    elif key == curses.KEY_DOWN:
        dy = 1
    elif key == curses.KEY_LEFT:
        dx = -1
    elif key == curses.KEY_RIGHT:
        dx = 1

    new_x = player.x + dx
    new_y = player.y + dy

    if 0 <= new_x < grid.width and 0 <= new_y < grid.height and grid.is_empty(new_x, new_y):
        player.x = new_x
        player.y = new_y