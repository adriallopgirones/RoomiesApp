from django.urls import path

from . import views

app_name = 'shared_list'

urlpatterns = [
    path('', views.purchases_list, name='purchases_list'),
    path('new_purchase/', views.new_purchase,  name="new_purchase")
]