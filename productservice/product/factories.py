import factory
from .models import Product

class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.Faker('word')
    description = factory.Faker('sentence')
    price = factory.Faker('pydecimal', left_digits=5, right_digits=2, positive=True)
    stock = factory.Faker('random_int', min=1, max=100)

