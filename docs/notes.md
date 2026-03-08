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


# Design Ideas:
    amount of mutations should cause some sort of penalty(maybe?)
    Some Mutations should boost stats while others create new tools for the player
    Function that applies mutations randomly and targetadely(Is that even a word???)?
    Mutation Class that handles what mutations a body currently stores?
    Items that induce mutations(need items class?)
    Enemies at some point i guess??


# HOW TO STRUCTURE MUTATIONS???
    An entities body should hold what mutations, mods and augments it has....
    a mutation should proably have a name, 
    and should probably provide a list of different effect functions such as on hit or on kill?
    would these functions be a part of the mutation class??? should this be replicated across the augment and biomod classes?

# Taking Stock:
3/6/2026
    -feelling like i want to abandon again... dont want to script and edit video, dont want to work on game, dont want to play something else
    solution?
        -work on something menial for 5 minutes, maybe add comments or something till i ether quit or keep working?
3/7/2026:
    -Im frustrated, it feels like more of the same retarded nonsense is kicking my shins in, ive decided im scrapping the current body system at least for now.
     Gemini has suggested a dictionary/yaml/json based approach and im gonna see where that takes me.