# urls.py
from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('adminPage/', views.adminPage, name='adminPage'),
    path('fieldOfficerPage/', views.fieldOfficerPage, name='fieldOfficerPage'),
]