from django.urls import path
from .views import (
    ProductListAPIView, ProductDetailAPIView, ProductCreateAPIView
)
urlpatterns = [
    path('list/', ProductListAPIView.as_view(), name='product-list'),
    path('<int:id>/', ProductDetailAPIView.as_view(), name='product-detail'),
    # path('<int:id>/update/', ProductDetailAPIView.as_view(), name='product-update'),
    # path('<int:id>/delete/', ProductDetailAPIView.as_view(), name='product-delete'),
    path('', ProductCreateAPIView.as_view(), name='product-create'),
]

