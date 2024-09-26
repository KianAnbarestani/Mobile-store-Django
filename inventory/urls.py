from django.urls import path
from . import views

urlpatterns = [
    path('brands/', views.brand_list, name='brand_list'),
    path('phones/', views.phone_list, name='phone_list'),
    path('brands/add/', views.add_brand, name='add_brand'),
    path('phones/add/', views.add_phone, name='add_phone'),
    path('phones/update/<int:pk>/', views.update_phone, name='update_phone'),
    path('phones/delete/<int:pk>/', views.delete_phone, name='delete_phone'),
    path('brands/update/<int:pk>/', views.update_brand, name='update_brand'),
    path('brands/delete/<int:pk>/', views.delete_brand, name='delete_brand'),
]
