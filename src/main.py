#src/main.py
import curses
import entity_factory
import data
from grid import Grid
from entity import Entity, Stats, Actor
from utils import update_stats
from renderer import render, render_debug
from input import handle_input

def main(stdscr):
    curses.curs_set(0)  # hide cursor
    stdscr.nodelay(False)
    stdscr.keypad(True)

    #Setup scene and player(will move this soon)
    grid = Grid(20, 10)
    player = Actor(1, 1, '@', (255, 255, 255), body_data=data.BODY_TEMPLATES["humanoid"])
    player.components["stats"] = Stats(5, 5, 5, 2)

    



    while True:
        stdscr.clear()
        render(stdscr, grid, player)
        render_debug(stdscr, player)
        stdscr.refresh()

        #lazy input handling(will fix later)
        key = stdscr.getch()
        if key == ord('q'):
            break
        if key == ord('a'):
            for part in player.body:
                if part["part_id"] == "arm" and part["mod_id"] is None:
                    part["mod_id"] = "muscle_max"
                    break
            update_stats(player) # <-- This is INSIDE the loop!
        #stupid teleport thing i added.
        if key == ord('t'):
            player.move(5, 5, grid)
  
        #movement handling
        handle_input(key, player, grid)

curses.wrapper(main)