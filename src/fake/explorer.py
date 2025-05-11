from model.explorer import Explorer
# fake data, replaced in Chapter 10 by a real database and SQL
_explorers = [
    Explorer(name="Claude Hande",
        country="FR",
        description="Scarce during full moons"),
    Explorer(name="Noah Weiser",
        country="DE",
        description="Myopic machete man"),
]

def get_all() -> list[Explorer]:
    """
    Get all explorers
    """
    return _explorers

def get_one(name: str) -> Explorer | None:
    """
    Get one explorer by name
    """
    for explorer in _explorers:
        if explorer.name == name:
            return explorer
    return None

def create(explorer: Explorer) -> Explorer:
    """
    Create a new explorer
    """
    _explorers.append(explorer)
    return explorer

def modify(explorer: Explorer) -> Explorer | None:
    """
    Modify an explorer
    """
    for i, e in enumerate(_explorers):
        if e.name == explorer.name:
            _explorers[i] = explorer
            return explorer
    return None

def replace(explorer: Explorer) -> Explorer | None:
    """
    Replace an explorer
    """
    for i, e in enumerate(_explorers):
        if e.name == explorer.name:
            _explorers[i] = explorer
            return explorer
    return None

def delete(name: str) -> bool:
    """
    Delete an explorer
    """
    for i, e in enumerate(_explorers):
        if e.name == name:
            del _explorers[i]
            return True
    return False