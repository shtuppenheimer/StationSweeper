#src/entity_factory.py
from enum import auto, Enum
import random
import modification_factory

#enums
class PartTypes(Enum):
    """Enum class containing body part types"""
    #will add hands and feet later if i feel like it
    HEAD = auto()
    TORSO = auto()
    ARM = auto()
    LEG = auto()

class Body:
    """Every actor entity will have a body, this body is a series of Lists which hold an actors current parts, 
    mutations, enhancements and augmentations"""
    def __init__(self, ):
        self.parts = []
        self.mutations = []
        self.cyber_augments = []
        self.bio_enhancements = []

    def __repr__(self):
        parts = [part.part_name for part in self.parts]
        mutations = [mut.name for mut in self.mutations]
        augments = [aug.name for aug in self.cyber_augments]
        bio = [b.name for b in self.bio_enhancements]
        return (f"Body(Parts={parts}, "
                f"Mutations={mutations}, "
                f"CyberAugments={augments}, "
                f"BioEnhancements={bio})")

class BodyParts:
    """Body parts are objects stored on an actors body, they allow for extra equipslots and other such statistics boosts"""
    def __init__(self, part_name, part_type):
        self.part_name = part_name
        self.part_type = part_type




#lazy template creator
def create_humanoid_body():

    body = Body()
    body.parts.append(BodyParts("Head", PartTypes.HEAD))
    body.parts.append(BodyParts("Torso", PartTypes.TORSO))
    body.parts.append(BodyParts("Left Arm", PartTypes.ARM))
    body.parts.append(BodyParts("Left Leg", PartTypes.LEG))
    body.parts.append(BodyParts("Right Arm", PartTypes.ARM))
    body.parts.append(BodyParts("Right Leg", PartTypes.LEG))
    return body

#lazy mutation tester
def add_mutation_to_body(entity):
    mutation = modification_factory.DermaMax()

    entity.components["body"].mutations.append(mutation)

    mutation.modify_stats(entity)
