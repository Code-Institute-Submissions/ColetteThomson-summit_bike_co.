from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_bikes, name="all_bikes")
]
