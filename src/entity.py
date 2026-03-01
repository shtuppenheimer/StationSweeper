# src/entity.py
from enum import auto, Enum

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

class Body:
    def __init__(self, parts):
        self.parts = parts

class BodyParts:
    def __init__(self, part_name, part_type):
        self.part_name = part_name
        self.part_type = part_type
class Modifications:
    pass

class AI:
    #TODO: Add ai nonsense
    pass


#enums
class PartTypes(Enum):
    HEAD = auto()
    TORSO = auto()
    ARM = auto()
    HAND = auto()
    FOOT = auto()
    LEG = auto()

     
    



