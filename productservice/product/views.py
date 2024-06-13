from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from drf_spectacular.utils import OpenApiExample, extend_schema
from .selectors import get_all_products, get_product_by_id, delete_product
from .serializers import ProductSerializer, CreateProductSerializer, UpdateProductSerializer
from .services import create_product, update_product, delete_product as delete_product_service
from .utils import format_response


class ProductListAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            products = get_all_products()
            serializer = ProductSerializer(products, many=True)
            response_data = format_response(success=True, data=serializer.data)
            return Response(response_data, status=status.HTTP_200_OK)
        except Exception as e:
            response_data = format_response(success=False, message=str(e), error_code=500)
            return Response(response_data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ProductDetailAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        try:
            product = get_product_by_id(id)
            if product is None:
                response_data = format_response(success=False, message='Product not found', error_code=404)
                return Response(response_data, status=status.HTTP_404_NOT_FOUND)
            serializer = ProductSerializer(product)
            response_data = format_response(success=True, data=serializer.data)
            return Response(response_data, status=status.HTTP_200_OK)
        except Exception as e:
            response_data = format_response(success=False, message=str(e), error_code=500)
            return Response(response_data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @extend_schema(
        request=UpdateProductSerializer,
        responses={200: ProductSerializer},
        examples=[
            OpenApiExample(
                'Example input',
                value={
                    'name': 'Updated Product Name',
                    'description': 'Updated product description.',
                    'price': '29.99',
                    'stock': 50
                }
            ),
        ],
    )
    def put(self, request, id):
        serializer = UpdateProductSerializer(data=request.data)
        if serializer.is_valid():
            try:
                updated_product = update_product(id, serializer.validated_data)
                if updated_product:
                    response_data = format_response(success=True, data=ProductSerializer(updated_product).data)
                    return Response(response_data, status=status.HTTP_200_OK)
                else:
                    response_data = format_response(success=False, message='Product not found', error_code=404)
                    return Response(response_data, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                response_data = format_response(success=False, message=str(e), error_code=500)
                return Response(response_data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        response_data = format_response(success=False, message='Invalid data', data=serializer.errors, error_code=400)
        return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            if delete_product_service(id):
                response_data = format_response(success=True, message='Product deleted successfully')
                return Response(response_data, status=status.HTTP_204_NO_CONTENT)
            else:
                response_data = format_response(success=False, message='Product not found', error_code=404)
                return Response(response_data, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            response_data = format_response(success=False, message=str(e), error_code=500)
            return Response(response_data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ProductCreateAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @extend_schema(
        request=CreateProductSerializer,
        responses={201: ProductSerializer},
        examples=[
            OpenApiExample(
                'Example input',
                value={
                    'name': 'Sample Product',
                    'description': 'This is a sample product description.',
                    'price': '19.99',
                    'stock': 100
                }
            ),
        ],
    )
    def post(self, request):
        serializer = CreateProductSerializer(data=request.data)
        if serializer.is_valid():
            try:
                product = create_product(serializer.validated_data)
                response_data = format_response(success=True, data=ProductSerializer(product).data)
                return Response(response_data, status=status.HTTP_201_CREATED)
            except Exception as e:
                response_data = format_response(success=False, message=str(e), error_code=500)
                return Response(response_data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        response_data = format_response(success=False, message='Invalid data', data=serializer.errors, error_code=400)
        return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

