from fastapi import APIRouter, Depends, FastAPI, status, Response
from sqlalchemy.orm import Session
from ..controllers import menu_items_ingredients as controller
from ..schemas import menu_items_ingredients as schema
from ..dependencies.database import engine, get_db

router = APIRouter(
    tags=['MenuItemsIngredients'],
    prefix="/menu_items_ingredients"
)


@router.post("/", response_model=schema.MenuItemIngredient)
def create(request: schema.MenuItemIngredientCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)


@router.get("/", response_model=list[schema.MenuItemIngredient])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)


@router.get("/{menu_item_id}/{ingredient_id}", response_model=schema.MenuItemIngredient)
def read_one(menu_item_id: int, ingredient_id: int, db: Session = Depends(get_db)):
    item_ids = [menu_item_id, ingredient_id]
    return controller.read_one(db, item_ids=item_ids)


@router.put("/{menu_item_id}/{ingredient_id}", response_model=schema.MenuItemIngredient)
def update(menu_item_id: int, ingredient_id: int, request: schema.MenuItemIngredientUpdate,
           db: Session = Depends(get_db)):
    item_ids = [menu_item_id, ingredient_id]
    return controller.update(db=db, request=request, item_ids=item_ids)


@router.delete("/{menu_item_id}/{ingredient_id}")
def delete(menu_item_id: int, ingredient_id: int, db: Session = Depends(get_db)):
    item_ids = [menu_item_id, ingredient_id]
    return controller.delete(db=db, item_ids=item_ids)
