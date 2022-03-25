from django.shortcuts import render
from .models import Product


def all_bikes(request):
    """ shows all bikes, including sorting and search queries """
    # to return all products from model Product
    all_bikes = Product.objects.all()
    # use 'context' to return data to template
    context = {
        'all_bikes': all_bikes,
    }

    return render(request, 'products/products.html', context)
