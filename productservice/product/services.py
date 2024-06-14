from .models import Product
from .cache import (
    set_cached_product, delete_cached_product, delete_cached_product_list, set_cached_product_list
)


def update_product(product_id, data):
    try:
        product = Product.objects.get(id=product_id)
        for key, value in data.items():
            setattr(product, key, value)
        product.save()
        set_cached_product(product_id, product)
        delete_cached_product_list()
        return product
    except Product.DoesNotExist:
        return None


def delete_product(product_id):
    try:
        product = Product.objects.get(id=product_id)
        product.delete()
        delete_cached_product(product_id)
        delete_cached_product_list()
        return True
    except Product.DoesNotExist:
        return False


def create_product(data):
    product = Product.objects.create(**data)
    return product

