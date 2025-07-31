from rest_framework import serializers
from .models import Department, Product

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name']

class ProductSerializer(serializers.ModelSerializer):   
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ('id',)  # Assuming 'id' is auto-generated or managed by the database