from .models import Product
from .cache import (
    get_cached_product, set_cached_product
)
from django.core.exceptions import ObjectDoesNotExist
import logging

logger = logging.getLogger(__name__)

def get_all_products():
    return Product.objects.all()


def get_product_by_id(product_id):
    try:
        product = Product.objects.get(id=product_id)
        return product
    except Product.DoesNotExist:
        return None


def delete_product(product_id):
    try:
        product = Product.objects.get(id=product_id)
        product.delete()
        return True
    except ObjectDoesNotExist:
        return False
