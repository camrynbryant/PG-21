from . import customers

#cd C:/Users/andmu/PycharmProjects/PG-21
#py -m uvicorn FinalProject.api.main:app --reload
def load_routes(app):
    app.include_router(customers.router)
