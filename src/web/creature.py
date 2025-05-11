from fastapi import APIRouter
from model.creature import Creature
from service.creature import service as creature_service

router = APIRouter(prefix="/creature", tags=["creature"])

@router.get("/")
def get_all():
    return creature_service.get_all()

@router.get("/{name}")
def get_one(name) -> Creature | None:
    return creature_service.get_one(name)

@router.post("/")
def create_one(creature: Creature) -> Creature:
    return creature_service.create_one(creature)

@router.patch("/")
def modify(creature: Creature) -> Creature:
    return creature_service.modify(creature)

@router.put("/")
def replace(creature: Creature) -> Creature:
    return creature_service.replace(creature)

@router.delete("/{name}")
def delete_one(name: str) -> bool:
    return creature_service.delete_one(name)
