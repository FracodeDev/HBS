from django.contrib import admin
from .models import *

# input categoryModel in panel admin 
admin.site.register(CategoryModel)

# input stockModel in panel admin
admin.site.register(StockModel)

# input productModel in panel admin
admin.site.register(ProductModel)

# input warehouseModel in panel admin
admin.site.register(WarehouseModel)

