from django.urls import path

from . import views

app_name = 'shared_list'

urlpatterns = [
    path('', views.purchases_list, name = 'purchases_list'),
    path('new_purchase/', views.new_purchase,  name = 'new_purchase'),
    path(r'delete_purchase/<int:pk>', views.delete_purchase, name = 'delete_purchase'),
    path(r'edit_purchase/<int:pk>', views.edit_purchase, name = 'edit_purchase'),
    path(r'pay_purchase/<int:pk>', views.pay_purchase, name = 'pay_purchase')
]