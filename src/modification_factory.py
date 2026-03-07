class BodyMods:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_hit(self, source, target):
        pass
    
    def on_kill(self, source, victim):
        pass
    
    def modify_stats(self, entity, stat_to_change, bonus):
        stats = entity.components.get("stats")
        if stats:
            if stat_to_change in stats.values:
                stats.values[stat_to_change] += bonus
    
    def __repr__(self):
        return f"Name: {self.name}, Description: {self.description}"



class Mutations(BodyMods):
    """Mutations are random changes in the body that usually happen outside the users control"""
    pass

class CyberneticAugmentations(BodyMods):
    """Augmentations are deliberate Cybernetic enhancements or changes to the body"""
    pass

class BioEnhancements(BodyMods):
    """Modifications are deliberate Biological enhancements or changes to the body"""
    pass


class DermaMax(Mutations):
    def __init__ (self):
        super().__init__(
            name= "Epi-DermaMax", 
            description= "Subject grows a thicker epidermal layer"                  
        )
    def modify_stats (self, entity,):
        super().modify_stats(entity= entity, stat_to_change= "DEF", bonus= 2)
