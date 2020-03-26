from django.db import models
from django.contrib.auth.models import User

class SharedList (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sharedlist", null=True)
    name = models.CharField(max_length=200, default="")

class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="purchase", null=True)
    shared_list = models.ForeignKey(SharedList, on_delete=models.CASCADE, null=True)
    product_name = models.CharField(max_length=200, default="")
    product_price = models.FloatField(default=0.0)

