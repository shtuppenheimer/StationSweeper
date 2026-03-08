# src/entity.py


class Entity:
    def __init__(self, x, y, glyph, colour):
        self.x = x
        self.y = y
        self.glyph = glyph
        self.colour = colour
        self.components = {}
        
class Actor(Entity):
    def __init__(self, x, y, glyph, colour, body_data = None):
        super().__init__(x, y, glyph, colour)
        self.body = [dict(part) for part in body_data] if body_data else []
        self.mutations = []

    
    def move(self, dx, dy, grid):
        self.x = max(0, min(grid.width-1, self.x +dx))
        self.y = max(0, min(grid.height-1, self.y +dy))


class Stats:
    def __init__(self, health, strength, defence, action_points):
        self.base = {
            "Health": health,
            "STR": strength,
            "DEF": defence,
            "AP": action_points
        }
        self.current = self.base.copy()
    def __repr__(self):
        return f"Stats: {self.current}"   


class AI:
    #TODO: Add ai nonsense
    pass




     
    



