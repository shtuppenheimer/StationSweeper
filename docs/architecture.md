Basics:
# Entity component system:
# WWK:
    its a system that asks what an entity HAS rather than what it IS
    components we need or will need for entity:
        STATS
        Position???(i think its safe to say every entity will have a position so maybe not this one)
        AI
        Body (an entity can have a body meaning it has... well a body)
    components wee need or will need for bodies which are a component of entities in and of themselves:
        Body Parts(straight forward, proably use a dictionary of enums to indicate limbs an entity has, we'll see)

# ACTION POINTS
key inspiration was quasimorph, like the freedom that action points gives the player to plan out moves rather than a traditional speed system.

# Mod System:
    mods seem to me like theyd be another instance of ECS where you have a base mod class and systems that affect mods rather than having every mod be a subclass



# need to figure out how to divide the screen properly so i can have message log and player info properly organized and whatnot.

what is a repr...: just a thing in classes that allow you to print stuff in the class in a neat way..

right so thats basically An ECS right there.