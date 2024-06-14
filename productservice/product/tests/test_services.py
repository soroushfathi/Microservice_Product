import pytest
from productservice.product.services import create_product
from productservice.product.models import Product
from productservice.product.tests.factories import ProductFactory

@pytest.mark.django_db
def test_create_product():
    # Define product data
    product_data = {
        "name": "Test Product",
        "description": "This is a test product.",
        "price": 99,
        "stock": 100
    }

    # Create a product using the service function
    product = create_product(product_data)

    # Fetch the product from the database
    fetched_product = Product.objects.get(id=product.id)

    # Assertions
    assert fetched_product.name == product_data['name']
    assert fetched_product.description == product_data['description']
    assert fetched_product.price == product_data['price']
    assert fetched_product.stock == product_data['stock']

    # Ensure the product is created in the database
    assert Product.objects.count() == 1

