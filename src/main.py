#src/main.py
import curses
import entity_factory
from grid import Grid
from entity import Entity, Stats

from renderer import render, render_debug
from input import handle_input

def main(stdscr):
    curses.curs_set(0)  # hide cursor
    stdscr.nodelay(False)
    stdscr.keypad(True)

    grid = Grid(20, 10)
    player = Entity(1, 1, '@', (255,255,255))
    player.components["stats"] = Stats(5, 5, 5, 2)
    player.components["body"] = entity_factory.create_humanoid_body()
    



    while True:
        stdscr.clear()
        render(stdscr, grid, player)
        render_debug(stdscr, player)
        stdscr.refresh()

        key = stdscr.getch()
        if key == ord('q'):
            break
        if key == ord('a'):
            entity_factory.add_mutation_to_body(player.components['body'])
            render_debug(stdscr, player)
        handle_input(key, player, grid)

curses.wrapper(main)