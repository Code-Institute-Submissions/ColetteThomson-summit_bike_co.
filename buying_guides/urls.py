from django.urls import path
from . import views

urlpatterns = [
    path('', views.what_is_a_mtb, name="what_is_a_mtb"),
    path('', views.mtb_sizing, name="mtb_sizing"),
]
