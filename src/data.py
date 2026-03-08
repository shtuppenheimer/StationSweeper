#src/data.py


#body Parts
BODY_PARTS = {
    "head": {
        "name": "Head",
        "type": "HEAD",
        "bonuses": {} 
    },
    "torso": {
        "name": "Torso",
        "type": "TORSO",
        "bonuses": {}
    },
    "arm": {
        "name": "Arm",
        "type": "ARM",
        "bonuses": {}
    },
    "leg": {
        "name": "Leg",
        "type": "LEG",
        "bonuses": {}
    }
}
#BioEnhancements
MOD_REGISTRY = {
    "muscle_max": {
        "name": "MuscleMax",
        "desc": "Hyper-dense muscle fibers.",
        "bonuses": {"STR": 5}
    },
    "derma_max": {
        "name": "Epi-DermaMax",
        "desc": "Thickened epidermal plating.",
        "bonuses": {"DEF": 3}
    },
    "adrenal_gland": {
        "name": "Adrenal Gland",
        "desc": "An oversized, overactive gland.",
        "bonuses": {"AP": 2}
    },
    "hyper_vitality": {
        "name": "Hyper-Vitality",
        "desc": "Rapidly mutating cellular structure.",
        "bonuses": {"Health": 20}
    }
}

# body templates

BODY_TEMPLATES = {
    "humanoid": [
        {"part_id": "head",  },
        {"part_id": "torso", },
        {"part_id": "arm",   },
        {"part_id": "arm",   },
        {"part_id": "leg",   },
        {"part_id": "leg",   },
    ],
    "dog": [
        {"part_id": "head",  },
        {"part_id": "torso", },
        {"part_id": "leg",   },
        {"part_id": "leg",   },
        {"part_id": "leg",   },
        {"part_id": "leg",   },
    ]
}