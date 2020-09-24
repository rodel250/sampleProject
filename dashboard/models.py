from django.db import models
from datetime import datetime

# Create your models here.

class Medicine(models.Model):
    dateRegistered = models.DateField(default = datetime.now)
    SKU = models.AutoField(primary_key=True)
    category = models.CharField(max_length = 100)
    genericName = models.CharField(max_length = 100)
    commonBrand = models.CharField(max_length  = 100)
    manufacturedDate = models.DateField(default = datetime.now)
    expiryDate = models.DateField(default = datetime.now)
    size = models.IntegerField()
    howToUse = models.TextField()
    sideEffects = models.TextField()
    price = models.DecimalField(max_digits = 10, decimal_places=2)
    noOfItems = models.IntegerField()
    images = models.ImageField(upload_to='upload/')
   

    class Meta:
        db_table = "Medicine"