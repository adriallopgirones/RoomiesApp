from django.contrib import admin

from .models import Purchase, SharedList

admin.site.register(Purchase)
admin.site.register(SharedList)