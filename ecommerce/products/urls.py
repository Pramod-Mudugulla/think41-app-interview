from django.urls import path
from .views import product_list, product_detail, DepartmentProductsView, DepartmentListView, DepartmentDetailView

urlpatterns = [
    path('products/', product_list, name='product-list'),
    path('products/<int:pk>/', product_detail, name='product-detail'),
    path('departments/<int:pk>/products/', DepartmentProductsView.as_view(), name='department-products'),
    path('departments/', DepartmentListView.as_view(), name='department-list'),
    path('departments/<int:pk>/', DepartmentDetailView.as_view(), name='department-detail'),
]
# <pk>  