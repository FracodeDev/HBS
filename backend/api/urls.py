from django.urls import path
from . import views

urlpatterns = [
    path('product',views.ProductCreateView.as_view()),
    path('product-list',views.ProductListView.as_view()),
    path('product/<int:pk>',views.ProductDetailView.as_view()),
    path('stock',views.StockCreateView.as_view()),
    path('warehouse',views.WarehouseCreateView.as_view()),
    path('warehouse-list',views.WarehouseListView.as_view()),
    path('stock/<int:pk>',views.StockDetailView.as_view()),
    path('stock-destroy/<int:pk>',views.StockDeleteView.as_view()),
]