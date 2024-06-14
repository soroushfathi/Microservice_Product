import pytest
from productservice.product.selectors import get_all_products, get_product_by_id
from productservice.product.tests.factories import ProductFactory

@pytest.mark.django_db
def test_get_all_products():
    ProductFactory.create_batch(3)

    products = get_all_products()

    assert products.count() == 3


@pytest.mark.django_db
def test_get_product_by_id():
    product = ProductFactory()
    fetched_product = get_product_by_id(product.id)

    assert fetched_product == product

    non_existent_id = 999
    fetched_product = get_product_by_id(non_existent_id)
    assert fetched_product is None

