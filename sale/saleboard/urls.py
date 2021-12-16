from django.urls import path

from . import views


app_name = 'saleboard'

urlpatterns = [
    path('', views.index, name='index'),
    path('item/<slug:slug>/', views.item_detail, name='item_detail'),
    path('item_create/', views.item_create, name='item_create'),
]
