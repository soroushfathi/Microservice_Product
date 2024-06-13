from django.urls import path, include

urlpatterns = [
    path('users/', include(('productservice.users.urls', 'users'))),
    path('auth/', include(('productservice.authentication.urls', 'auth'))),
    path('products/', include(('productservice.product.urls', 'products')))
]
