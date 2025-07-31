from django.shortcuts import render
from rest_framework.response import Response
from .models import Product, Department
from django.shortcuts import get_object_or_404
from .serializers import ProductSerializer, DepartmentSerializer
from rest_framework.decorators import api_view, APIView
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

class DepartmentListView(APIView):
    def get(self, request):
        departments = Department.objects.all()
        serializer = DepartmentSerializer(departments, many=True)
        return Response(serializer.data)

class DepartmentDetailView(APIView):
    def get(self, request, pk):
        department = get_object_or_404(Department, pk=pk)
        serializer = DepartmentSerializer(department)
        return Response(serializer.data)

class DepartmentProductsView(APIView):
    def get(self, request, pk):
        department = get_object_or_404(Department, pk=pk)
        products = Product.objects.filter(department=department)

        paginator = PageNumberPagination()
        paginated_products = paginator.paginate_queryset(products, request)
        serializer = ProductSerializer(paginated_products, many=True)

        return paginator.get_paginated_response(serializer.data)
