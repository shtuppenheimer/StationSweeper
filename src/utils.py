#utils.py

from data import BODY_PARTS, MOD_REGISTRY

def update_stats(actor):
    stats_component = actor.components.get("stats")
    if not stats_component:
        return
    
    stats_component.current = stats_component.base.copy()

    for part in actor.body:
        part_data = BODY_PARTS.get(part["part_id"])
        if part_data:
            for stat, value in part_data.get("bonuses", {}).items():
                stats_component.current[stat]+=value

        mod_id = part.get("mod_id")
        if mod_id:
            mod_data = MOD_REGISTRY.get(mod_id)
            if mod_data:
                for stat, value in mod_data.get("bonuses", {}).items():
                    stats_component.current[stat]+=value