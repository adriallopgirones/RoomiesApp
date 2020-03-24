from django.db import models

class Purchase(models.Model):
    product_name = models.CharField(max_length=200, default="")
    product_price = models.FloatField(default=0.0)

