from .models import Product
from django.core.exceptions import ObjectDoesNotExist


def get_all_products():
    return Product.objects.all()


def get_product_by_id(product_id):
    try:
        return Product.objects.get(id=product_id)
    except ObjectDoesNotExist:
        return None


def delete_product(product_id):
    try:
        product = Product.objects.get(id=product_id)
        product.delete()
        return True
    except ObjectDoesNotExist:
        return False
