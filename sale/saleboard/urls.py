from django.urls import path

from . import views


app_name = 'saleboard'

urlpatterns = [
    path('', views.index, name='index'),
]
