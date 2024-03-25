from typing import List, Optional
from fastapi import APIRouter
from crud import get_all_products, get_product_by_id
from models import Product

product_router = APIRouter()


@product_router.get("/products")
def get_products() -> List[Product]:
    products = get_all_products()
    return products


@product_router.get("/products/{product_id}", response_model=Optional[Product])
def get_product(product_id: int) -> Product:
    product = get_product_by_id(product_id)
    return product
