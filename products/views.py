from django.shortcuts import render, get_object_or_404
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


def bike_detail(request, product_id):
    """ shows individual bike details """
    # to return a product from model Product, else 404 error message
    product = get_object_or_404(Product, pk=product_id)
    # use 'context' to return data to template
    context = {
        'product': product,
    }

    return render(request, 'products/bike_detail.html', context)
