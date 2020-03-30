from django.db import models
from django.conf import settings

class SharedList (models.Model):
    group_id = models.CharField(max_length=200, unique=True, default="")
    name = models.CharField(max_length=200, default="")

class Purchase(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="purchase", null=True)
    shared_list = models.ForeignKey(SharedList, on_delete=models.CASCADE, null=True)
    product_name = models.CharField(max_length=200, default="")
    product_price = models.FloatField(default=0.0)
    purchased = models.BooleanField(default=False)
    receivers = models.CharField(max_length=500, default="")