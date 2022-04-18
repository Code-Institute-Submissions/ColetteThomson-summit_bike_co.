from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_bikes, name="products"),
    # use 'int', to prevent a view error (i.e. when navigating to products/add
    # and django interpretation of the string 'add' as a 'product_id')
    path('<int:product_id>/', views.bike_detail, name="bike_detail"),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product,
         name='delete_product'),
]
