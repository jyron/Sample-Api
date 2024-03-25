"""Test Router Functions."""

from fastapi.testclient import TestClient
from typing import List, Dict
from main import app
from models import Product
from crud import get_all_products, get_product_by_id

client = TestClient(app=app)


# Test Routers
def test_get_products():
    response = client.get("/products")
    assert response.status_code == 200
    assert isinstance(response.json(), List)
    assert all(isinstance(item, dict) for item in response.json())


def test_get_product():
    response = client.get("/products/1")
    product = Product(**response.json())
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    for key in Product.model_fields.keys():
        assert hasattr(product, key)
