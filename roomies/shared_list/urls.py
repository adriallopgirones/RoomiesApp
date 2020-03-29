from django.urls import path

from . import views

app_name = 'shared_list'

urlpatterns = [
    path('', views.purchases_list, name = 'purchases_list'),
    path('new_purchase/', views.new_purchase,  name = 'new_purchase'),
    path(r'delete_purchase/(?P<pk>[0-9]+)/$', views.delete_purchase, name = 'delete_purchase'),
    path(r'pay_purchase/<int:pk>', views.pay_purchase, name = 'pay_purchase')
]