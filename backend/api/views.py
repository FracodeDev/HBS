from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import permissions 
from rest_framework import generics 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .models import *
from .serializers import *


class StockCreateView(generics.CreateAPIView):
    """
    ای پی آی ایجاد یک موجودی برای محصول 
    """
    queryset = StockModel.objects.all()
    serializer_class = StockSerializer
    authentication_classes = [JWTAuthentication]

class ProductCreateView(generics.CreateAPIView):
    """
    ای پی آی ایجاد یک محصول 
    """
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [JWTAuthentication]

class WarehouseCreateView(generics.CreateAPIView):
    """
    ای پی آی ساخت یک انبار برای محصولات 
    """
    queryset = WarehouseModel.objects.all()
    serializer_class = WarehouseSerializer
    authentication_classes = [JWTAuthentication]

class ProductListView(generics.ListAPIView):
    """
    ای پی آی لیست تمامی محصولات ساخته شده 
    """
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

class WarehouseListView(generics.ListAPIView):
    """
    ای پی آی لیست تمامی انبار ها با محصولات آنها 
    """
    queryset = WarehouseModel.objects.all()
    serializer_class = WarehouseSerializer
    lookup_field = 'pk'

class ProductDetailView(generics.RetrieveAPIView):
    """
    ای پی آی مشاهده اطلاعات یک محصول با آیدی آن محصول 
    """
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

class StockDetailView(generics.RetrieveAPIView):
    """
    ای پی آی مشاهده مشخصات یک موجودی 
    """
    queryset = StockModel.objects.all()
    serializer_class = StockSerializer
    lookup_field = 'pk'

class StockDeleteView(generics.DestroyAPIView):
    """
    ای پی آی حذف کردن یک موجودی مشخص شده 
    """
    queryset = StockModel.objects.all()
    serializer_class = StockSerializer    
    lookup_field = 'pk'
    

    

