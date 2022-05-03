from django.urls import path
from . import views

urlpatterns = [
    path('', views.what_is_a_mtb, name="what_is_a_mtb"),
    path('mtb_sizing', views.mtb_sizing, name="mtb_sizing"),
]
