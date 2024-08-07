from . import customers, orders, payments, promotions, reviews, ingredients, credit_cards, menu_items, \
    customers_payments_promotions, orders_menu_items, menu_items_ingredients


#cd C:/Users/andmu/PycharmProjects/PG-21
#py -m uvicorn FinalProject.api.main:app --reload
def load_routes(app):
    app.include_router(customers.router)
    app.include_router(orders.router)
    app.include_router(payments.router)
    app.include_router(promotions.router)
    app.include_router(reviews.router)
    app.include_router(ingredients.router)
    app.include_router(credit_cards.router)
    app.include_router(menu_items.router)
    app.include_router(customers_payments_promotions.router)
    app.include_router(orders_menu_items.router)
    app.include_router(menu_items_ingredients.router)
