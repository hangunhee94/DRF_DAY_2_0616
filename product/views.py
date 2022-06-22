from urllib import response
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from datetime import datetime
from django.db.models import Q

from product.models import Product as ProductModel


from product.serializers import ProductSerializer

# Create your views here.
class ProductView(APIView):

    def get(self, request):
        today = datetime.now()
        products = ProductModel.objects.filter(
            Q(exposure_start_date__lte=today, exposure_end_date__gte=today, )|
            Q(user=request.user)
        )

        serialized_data = ProductSerializer(products, many=True).data

        return Response(serialized_data, status=status.HTTP_200_OK)

    def post(self, request):
        request.data['user'] =request.user.id

        product_serializer = ProductSerializer(data=request.data)

        if product_serializer.is_valid():
            product_serializer.save()

            return Response(product_serializer.data, status=status.HTTP_200_OK)
        else:
            Response(product_serializer.errors, stauts=status.HTTP_400_BAD_REQUEST)


    # patch로 사용할때는 보통 바뀐 부분만 보냄(포스트맨) ex) title만 수정시 title만 보낸다
    def put(self, request, product_id):
        product = ProductModel.objects.get(id=product_id)
        product_serializer = ProductSerializer(product, data=request.data, partial=True)
        
        if product_serializer.is_valid():
            product_serializer.save()

            return Response(product_serializer.data, status=status.HTTP_200_OK)
        else:
            Response(product_serializer.errors, stauts=status.HTTP_400_BAD_REQUEST)