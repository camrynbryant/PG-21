from . import orders, reviews, customers, credit_cards, \
    customers_payments_promotions, ingredients, menu_items, menu_items_ingredients, orders_menu_items, payments, \
    promotions, resources

from ..dependencies.database import engine


def index():
    customers.Base.metadata.create_all(engine)
    #orders.Base.metadata.create_all(engine)
    #credit_cards.Base.metadata.create_all(engine)
    #customers.Base.metadata.create_all(engine)
    #customers_payments_promotions.Base.metadata.create_all(engine)
    #ingredients.Base.metadata.create_all(engine)
    #menu_items.Base.metadata.create_all(engine)
    #menu_items_ingredients.Base.metadata.create_all(engine)
    #orders_menu_items.Base.metadata.create_all(engine)
    #payments.Base.metadata.create_all(engine)
    #promotions.Base.metadata.create_all(engine)
    reviews.Base.metadata.create_all(engine)


