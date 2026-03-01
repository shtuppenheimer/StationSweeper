# src/grid.py
class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = [['.' for _ in range(width)] for _ in range(height)]

    def add_wall(self, x, y):
        self.cells[y][x] = '#'

    def is_empty(self, x, y):
        return self.cells[y][x] == '.'