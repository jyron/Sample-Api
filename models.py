from pydantic import BaseModel


class Product(BaseModel):
    name: str
    description: str
    category: str
    price: float
