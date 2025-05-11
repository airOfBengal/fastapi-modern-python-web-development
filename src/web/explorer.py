from fastapi import APIRouter
from model.explorer import Explorer
from service.exporer import service as explorer_service

router = APIRouter(prefix="/explorer")

@router.get("/")
def get_all():
    return explorer_service.get_all()

@router.get("/{name}")
def get_one(name) -> Explorer | None:
    
    return explorer_service.get_one(name)

@router.post("/")
def create_one(explorer: Explorer) -> Explorer:
    return explorer_service.create_one(explorer)

@router.patch("/")
def modify(explorer: Explorer) -> Explorer:
    return explorer_service.modify(explorer)

@router.put("/")
def replace(explorer: Explorer) -> Explorer:
    return explorer_service.replace(explorer)    

@router.delete("/{name}")
def delete_one(name: str) -> bool:
    return explorer_service.delete_one(name)
