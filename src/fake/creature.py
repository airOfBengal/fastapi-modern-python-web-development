from model.creature import Creature

# fake data, until we use a real database and SQL
_creatures = [
Creature(name="Yeti",
aka="Abominable Snowman",
country="CN",
area="Himalayas",
description="Hirsute Himalayan"),
Creature(name="Bigfoot",
description="Yeti's Cousin Eddie",
country="US",
area="*",
aka="Sasquatch"),
]

def get_all() -> list[Creature]:
    """
    Get all creatures
    """
    return _creatures

def get_one(name: str) -> Creature | None:
    """
    Get one creature by name
    """
    for creature in _creatures:
        if creature.name == name:
            return creature
    return None

def create(creature: Creature) -> Creature:
    """
    Create a new creature
    """
    _creatures.append(creature)
    return creature

def modify(creature: Creature) -> Creature | None:
    """
    Modify a creature
    """
    for i, e in enumerate(_creatures):
        if e.name == creature.name:
            _creatures[i] = creature
            return creature
    return None

def replace(creature: Creature) -> Creature | None:
    """
    Replace a creature
    """
    for i, e in enumerate(_creatures):
        if e.name == creature.name:
            _creatures[i] = creature
            return creature
    return None

def delete(name: str) -> bool:
    """
    Delete a creature
    """
    for i, e in enumerate(_creatures):
        if e.name == name:
            del _creatures[i]
            return True
    return False

