from .models import Product


def create_product(data):
    return Product.objects.create(**data)


def update_product(product_id, data):
    try:
        product = Product.objects.get(id=product_id)
        for key, value in data.items():
            setattr(product, key, value)
        product.save()
        return product
    except Product.DoesNotExist:
        return None


def delete_product(product_id):
    try:
        product = Product.objects.get(id=product_id)
        product.delete()
        return True
    except Product.DoesNotExist:
        return False
