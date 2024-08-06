from fastapi import APIRouter, Depends, FastAPI, status, Response
from sqlalchemy.orm import Session
from ..controllers import menuItem as controller
from ..schemas import menuItem as schema
from ..dependencies.database import engine, get_db

router = APIRouter(
    tags=['Menu Items'],
    prefix="/menu-items"
)

@router.post("/", response_model=schema.MenuItem)
def create(request: schema.MenuItemCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)

@router.get("/", response_model=list[schema.MenuItem])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/{menu_item_id}", response_model=schema.MenuItem)
def read_one(menu_item_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, menu_item_id=menu_item_id)

@router.put("/{menu_item_id}", response_model=schema.MenuItem)
def update(menu_item_id: int, request: schema.MenuItemUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, menu_item_id=menu_item_id)

@router.delete("/{menu_item_id}")
def delete(menu_item_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, menu_item_id=menu_item_id)
