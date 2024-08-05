from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import menu_items_ingredients as model
from sqlalchemy.exc import SQLAlchemyError


def create(db: Session, request):
    new_item = model.MenuItemIngredient(
        menu_item_id = request.menu_item_id,
        ingredient_id = request.ingredient_id
    )


def read_all(db: Session):
    try:
        result = db.query(model.MenuItemIngredient).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return result


def read_one(db: Session, item_ids):
    """

    :param db:
    :param item_ids: an object that contains the 2 attributes which make up the primary key of the
    menu_items_ingredients table. These 2 attributes include menu_item_id and ingredient_id.
    :return:
    """
    try:
        menu_item_id = item_ids.menu_item_id
        ingredient_id = item_ids.ingredient_id

        item = (db.query(model.MenuItemIngredient).
                filter(model.MenuItemIngredient.menu_item_id == menu_item_id,
                       model.MenuItemIngredient.ingredient_id == ingredient_id).first())
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail="Menu_item_id or Ingredient_id not found!")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item

def update(db: Session, item_ids, request):
    try:
        menu_item_id = item_ids.menu_item_id
        ingredient_id = item_ids.ingredient_id

        item = (db.query(model.MenuItemIngredient).
                filter(model.MenuItemIngredient.menu_item_id == menu_item_id,
                       model.MenuItemIngredient.ingredient_id == ingredient_id))
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail="Menu_item_id or Ingredient_id not found!")
        update_data = request.dict(exclude_unset=True)
        item.update(update_data, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item.first()


def delete(db: Session, item_ids):
    try:
        menu_item_id = item_ids.menu_item_id
        ingredient_id = item_ids.ingredient_id

        item = (db.query(model.MenuItemIngredient).
                filter(model.MenuItemIngredient.menu_item_id == menu_item_id,
                       model.MenuItemIngredient.ingredient_id == ingredient_id))
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail="Menu_item_id or Ingredient_id not found!")
        item.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


