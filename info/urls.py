from django.urls import path
from . import views

urlpatterns = [
    path('', views.who_we_are, name="who_we_are"),
    path('cycle_to_work', views.cycle_to_work, name="cycle_to_work"),
    path('terms_conditions', views.terms_conditions, name="terms_conditions"),
]
