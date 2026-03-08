# src/renderer.py
def render(stdscr, grid, player):
    for y in range(grid.height):
        for x in range(grid.width):
            char = player.glyph if (x, y) == (player.x, player.y) else grid.cells[y][x]
            stdscr.addch(y, x, char)

def render_debug(stdscr, player):
#will change to be agnostic in future
    stdscr.addstr(13,0, f"{player.components.get('stats')}")
    anatomy_list = [f"{p['part_id']}" for p in player.body]


    stdscr.addstr(14, 0, f"Body: {', '.join(anatomy_list)}")