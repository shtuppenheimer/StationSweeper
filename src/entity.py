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
        self.health = health
        self.strength =  strength
        self.defence = defence
        self.action_points = action_points
    def __repr__(self):
        return f"Stats: health: {self.health}, strength: {self.strength}, defence: {self.defence}, action points: {self.action_points}"   


class AI:
    #TODO: Add ai nonsense
    pass




     
    



