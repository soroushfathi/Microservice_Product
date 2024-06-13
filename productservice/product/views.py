from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .selectors import get_all_products
from .serializers import ProductSerializer
from .utils import format_response


class ProductListAPIView(APIView):
    def get(self, request):
        try:
            products = get_all_products()
            serializer = ProductSerializer(products, many=True)
            response_data = format_response(success=True, data=serializer.data)
            return Response(response_data, status=status.HTTP_200_OK)
        except Exception as e:
            response_data = format_response(success=False, message=str(e), error_code=500)
            return Response(response_data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

