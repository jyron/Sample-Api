"""Crud functions to interact with the database."""

import json
from typing import List, Optional

from pydantic import ValidationError

from models import Product


def get_all_products_old() -> List[Product]:
    """Retrieves all products from the json file."""
    with open("data.json") as file:
        data = json.load(file)
    products_data = data.get("products", [])
    products = [Product(**product) for product in products_data]
    return products


def get_all_products() -> List[Product]:
    """Retrieves all products from the json file."""
    with open("data.json") as file:
        data = json.load(file)

    products_data = data.get("products", [])
    products = []
    for product_data in products_data:
        try:
            product_instance = Product(**product_data)
            products.append(product_instance)
        except ValidationError as e:
            print(f"Validation error creating Product instance: {e}")
        except Exception as e:
            print(f"Error creating Product instance: {e}")
    return products


def get_product_by_id(product_id: int) -> Optional[Product]:
    """Retrieves a product from the json file based on its ID."""
    with open("data.json") as file:
        data = json.load(file)
    products_data = data.get("products", [])
    for product in products_data:
        if product.get("id") == product_id:
            return Product(**product)
    return None
