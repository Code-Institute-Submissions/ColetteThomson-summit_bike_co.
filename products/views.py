from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
# to prevent product access via typed urls
from django.contrib.auth.decorators import login_required
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
                # use variable 'sortkey' to preserve original
                # field 'bike_model'
                sortkey = 'lower_bike_model'
                # use annotate for case-insensitive sorting
                products = products.annotate(lower_bike_model=Lower
                                             ('bike_model'))

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
            products = products. \
                filter(classification__name__in=classifications)
            classifications = Classification.objects. \
                filter(name__in=classifications)

        if 'q' in request.GET:
            query = request.GET['q']
            # if user has not entered search criteria
            if not query:
                # display error message to user
                messages.error(request, "Please enter your search criteria")
                # redirect user back to 'all bikes' page
                return redirect(reverse('products'))

            # search query is contained in 'bike_model' or 'type' fields
            queries = Q(bike_model__icontains=query) | \
                Q(type__icontains=query) | Q(material__icontains=query) | \
                Q(discipline__icontains=query)
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
    # render statement
    return render(request, 'products/products.html', context)


def bike_detail(request, product_id):
    """ shows individual bike details """
    # to return a product from model Product, else 404 error message
    product = get_object_or_404(Product, pk=product_id)
    # use 'context' to return data to template
    context = {
        'product': product,
    }
    # render statement
    return render(request, 'products/bike_detail.html', context)


# check if user is logged in, if not redirect to login page
@login_required
def add_product(request):
    """ add a product to the store """
    # if user is not a superuser
    if not request.user.is_superuser:
        # display error message
        messages.error(request, 'Sorry, only store owners can do that.')
        # redirect back to home page
        return redirect(reverse('home'))

    if request.method == 'POST':
        # create instance of ProductForm from request.post
        # use request.files to capture product image (if submitted)
        form = ProductForm(request.POST, request.FILES)
        # check form is valid, if so then save
        if form.is_valid():
            product = form.save()
            # display success message
            messages.info(request, 'Successfully added product!')
            # redirect to bike_detail using product id
            return redirect(reverse('bike_detail', args=[product.id]))
        else:
            # if form not valid, display message to user
            messages.error(request, 'Failed to add product. \
                           Please ensure the form is valid.')
    else:
        # display empty form
        form = ProductForm()

    # which template to use and the context
    template = 'products/add_product.html'
    context = {
        'form': form,
    }
    # render statement
    return render(request, template, context)


# check if user is logged in, if not redirect to login page
@login_required
def edit_product(request, product_id):
    """ edit an existing product """
    # if user is not a superuser
    if not request.user.is_superuser:
        # display error message
        messages.error(request, 'Sorry, only store owners can do that.')
        # redirect back to home page
        return redirect(reverse('home'))

    # pre-fill form with existing product info
    product = get_object_or_404(Product, pk=product_id)
    # post handler
    if request.method == 'POST':
        # create instance of ProductForm from request.post
        # use request.files to capture product image (if submitted)
        # specific instance to be updated is product above
        form = ProductForm(request.POST, request.FILES, instance=product)
        # check form is valid, if so then save
        if form.is_valid():
            form.save()
            # display success message
            messages.info(request, 'Successfully updated product!')
            # redirect to bike_detail using product id
            return redirect(reverse('bike_detail', args=[product.id]))
        else:
            # if form not valid, display message to user
            messages.error(request, 'Failed to update product. Please \
                        ensure the form is valid.')
    else:
        # instantiate form using the product
        form = ProductForm(instance=product)
        # display info message to user
        messages.info(request, f'You are editing {product.bike_model}')

    # which template to use and the context
    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }
    # render statement
    return render(request, template, context)


# check if user is logged in, if not redirect to login page
@login_required
def delete_product(request, product_id):
    """ delete a product """
    # if user is not a superuser
    if not request.user.is_superuser:
        # display error message
        messages.error(request, 'Sorry, only store owners can do that.')
        # redirect back to home page
        return redirect(reverse('home'))

    # call product using product id
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    # display info message to user
    messages.info(request, 'Product deleted!')
    # redirect back to products page
    return redirect(reverse('products'))


def contact_us(request):
    """ return 'contact_us' page """
    return render(request, 'info/contact_us.html')


def what_is_a_mtb(request):
    """ return 'what is a mountain bike?' page """
    return render(request, 'buying_guides/what_is_a_mtb.html')
