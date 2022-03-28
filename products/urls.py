from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_bikes, name="products"),
    path('<product_id>', views.bike_detail, name="bike_detail"),
]
