from django.urls import path, include

from . import views

app_name = 'user_system'

urlpatterns = [
    path('signup/', views.SignUp, name='signup'),
    path('login/', views.login_request, name='login_request'),
    path('logout/', views.logout_request, name='logout_request'),
    path('join_group/', views.join_group, name='join_group'),
    path('new_group/', views.new_group, name='new_group')
]