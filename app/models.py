from django.db import models

# Create your models here.

class Productcategory(models.Model):
    prod_cat_id = models.IntegerField(primary_key=True)
    prod_cat_name = models.CharField(max_length=100)

    def __str__(self):
        return self.prod_cat_name
    
class Product(models.Model):
    prod_id = models.IntegerField(primary_key=True)
    prod_cat_name = models.ForeignKey(Productcategory,on_delete=models.CASCADE)
    prod_name = models.CharField(max_length=100)
    prod_brand = models.CharField(max_length=100)
    prod_price = models.IntegerField()

    def __str__(self):
        return self.prod_name