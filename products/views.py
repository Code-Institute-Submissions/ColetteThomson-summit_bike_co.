from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
# Q needed to generate search query if query isn't blank
from django.db.models import Q
from .models import Product


def all_bikes(request):
    """ shows all bikes, including sorting and search queries """
    # to return all products from model Product
    products = Product.objects.all()
    query = None # take out after testing to see if search works

    # if user has entered search criteria
    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            # if user has not entered search criteria
            if not query:
                # display error message to user
                messages.error(request, "Please enter your search criteria")
                # redirect user back to 'all bikes' page
                return redirect(reverse('products'))

            # search query is contained in 'bike_model' or 'type' fields
            queries = Q(bike_model__icontains=query) | Q(type__icontains=query)
            # queries are filtered
            products = products.filter(queries)

    # use 'context' to return data to template
    context = {
        'products': products,
        'search_term' : query,
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
