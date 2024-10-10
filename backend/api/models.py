from django.db import models

class CategoryModel(models.Model):
    description = models.TextField(blank = True , null = True)
    name = models.CharField(max_length = 35)

class StockModel(models.Model):
    name = models.CharField(max_length = 35)
    value = models.CharField(max_length = 50)
    
class ProductModel(models.Model):
    name = models.CharField(max_length = 40)
    description = models.TextField(blank = True , null = True)
    imageproduct = models.ImageField(upload_to=None, height_field=None , width_field=None , max_length=100) 
    time = models.DateTimeField(auto_now = False , auto_now_add = False)
    stock = models.ForeignKey(StockModel , on_delete = models.CASCADE)

class WarehouseModel(models.Model):
    name = models.CharField(max_length = 40)
    warehouse_number = models.CharField(max_length = 25)
    address = models.TextField(blank = True , null = True)
    time = models.DateTimeField(auto_now=False , auto_now_add=False)
    product = models.ForeignKey(ProductModel , on_delete = models.CASCADE)
    category = models.ForeignKey(CategoryModel , on_delete = models.CASCADE)
    



