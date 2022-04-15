from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
# Q needed to generate search query if query isn't blank
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Classification
from .forms import ProductForm


def all_bikes(request):
    """ shows all bikes, including sorting and search queries """
    # to return all products from model Product
    products = Product.objects.all()
    # take out after testing to see if search works
    query = None
    classifications = None
    sort = None
    direction = None

    # if user has entered search criteria
    if request.GET:
        # if get parameters contain 'sort'
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            # set 'sort' from 'none' to sortkey
            sort = sortkey
            if sortkey == 'bike_model':
                # use variable 'sortkey' to preserve original field 'bike_model'
                sortkey = 'lower_bike_model'
                # use annotate for case-insensitive sorting
                products = products.annotate(lower_bike_model=Lower('bike_model'))

            if sortkey == 'classification':
                # to allow drilling into related model (__)
                sortkey = 'classification__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                # check if direction is 'descending, if so add '-'
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            # sort the product using order_by method
            products = products.order_by(sortkey)

        if 'classification' in request.GET:
            classifications = request.GET['classification'].split(',')
            products = products.filter(classification__name__in=classifications)
            classifications = Classification.objects.filter(name__in=classifications)

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

    # return results to template
    current_sorting = f'{sort}_{direction}'

    # use 'context' to return data to template
    context = {
        'products': products,
        'search_term': query,
        'current_classifications': classifications,
        'current_sorting': current_sorting,
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


def add_product(request):
    """ add a product to the store """
    form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
