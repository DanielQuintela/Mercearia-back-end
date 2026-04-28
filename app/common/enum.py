from enum import Enum

class TableName(Enum):
    PRODUCTS = "products"
    USERS = "users"
    PRODUCERS = "producers"
    CATEGORIES = "categories"
    PROMOTIONS = "promotions"
    

class LogAction(Enum):
    CREATE = "CREATE"
    UPDATE = "UPDATE"
    DELETE = "DELETE"
