from django.shortcuts import render
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.pagination import PageNumberPagination


@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    paginator = PageNumberPagination()
    paginator.page_size = 10  # or leave it to settings
    
    result_page = paginator.paginate_queryset(products, request)
    serializer = ProductSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)



@api_view(['GET'])
def product_detail(request, pk):
    """
    Retrieve a product by its ID.
    """
    try:
        # Validate ID
        pk = int(pk)
    except ValueError:
        return Response(
            {"error": "Invalid product ID."},
            status=status.HTTP_400_BAD_REQUEST
        )

    try:
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    except Product.DoesNotExist:
        return Response(
            {"error": "Product not found."},
            status=status.HTTP_404_NOT_FOUND
        )