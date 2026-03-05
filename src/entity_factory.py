#src/entity_factory.py
from enum import auto, Enum
#enums
class PartTypes(Enum):
    #will add hands and feet later if i feel like it
    HEAD = auto()
    TORSO = auto()
    ARM = auto()
    LEG = auto()

class Body:
    def __init__(self, ):
        self.parts = []
    def __repr__(self):
        for part in self.parts:
            part_names = [part.part_name for part in self.parts]
            return f"Body(Parts = {part_names})"

class BodyParts:
    def __init__(self, part_name, part_type):
        self.part_name = part_name
        self.part_type = part_type

class Modifications:
    pass


def create_humanoid_body():
    body = Body()
    body.parts.append(BodyParts("Head", PartTypes.HEAD))
    body.parts.append(BodyParts("Torso", PartTypes.TORSO))
    body.parts.append(BodyParts("Left Arm", PartTypes.ARM))
    body.parts.append(BodyParts("Left Leg", PartTypes.LEG))
    body.parts.append(BodyParts("Right Arm", PartTypes.ARM))
    body.parts.append(BodyParts("Right Leg", PartTypes.LEG))
    return body