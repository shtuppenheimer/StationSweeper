# src/entity.py


class Entity:
    def __init__(self, x, y, glyph, colour):
        self.x = x
        self.y = y
        self.glyph = glyph
        self.colour = colour
        self.components = {}

#components (to be moved later)
class Stats:
    def __init__(self, health, strength, defence, action_points):
        self.values = {
            "Health": health,
            "STR": strength,
            "DEF": defence,
            "AP": action_points
        }
        
    def __repr__(self):
        return f"Stats: {self.values}"   


class AI:
    #TODO: Add ai nonsense
    pass




     
    



