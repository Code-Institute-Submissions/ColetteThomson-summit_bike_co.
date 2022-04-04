from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages
from products.models import Product


def view_bag(request):
    """ view products in shopping bag """
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ add product quantity to shopping bag """

    # get product from model Product
    product = Product.objects.get(pk=item_id)
    # obtain quantity required (convert to integer from string)
    quantity = int(request.POST.get('quantity'))
    # redirect to user's current location, after item is added to bag
    redirect_url = request.POST.get('redirect_url')
    # set size
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']

    """
    store bag info in a http 'session' allowing user to continue browsing &
    adding items to bag without losing contents of their bag
    """

    # get bag variable if it exists or create one if not
    bag = request.session.get('bag', {})

    # check if product with sizes is being added
    if size:
        if item_id in list(bag.keys()):
            """
            if item already in the bag, check if another item of
            the same id and same size already exists
            """
            if size in bag[item_id]['items_by_size'].keys():
                # increment quantity for chosen size
                bag[item_id]['items_by_size'][size] += quantity
            else:
                # set item to chosen quantity as is a new size for that item
                bag[item_id]['items_by_size'][size] = quantity
        else:
            """
            if items not already in bag, add them using dictionary,
            (for multiple items with same id, but different sizes)
            """
            bag[item_id] = {'items_by_size': {size: quantity}}

    else:
        # if item has no size
        if item_id in list(bag.keys()):
            # increment its quantity
            bag[item_id] += quantity
        else:
            # if no bag, create one with item and quantity
            bag[item_id] = quantity
            # confirmation message to user for product added to bag
            messages.success(request, f'Added {product.bike_model} to your bag')

    # overwrite session with updated variable
    request.session['bag'] = bag
    # redirect user back to their original page
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """ edit quantity of specified product to specified amount """
    # obtain quantity required (convert to integer from string)
    quantity = int(request.POST.get('quantity'))
    # set size
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']

    # get bag variable if it exists or create one if not
    bag = request.session.get('bag', {})

    # check if product with sizes is being added
    if size:
        if quantity > 0:
            # drill into 'items-by-size' dictionary and update item's quantity
            bag[item_id]['items_by_size'][size] = quantity
        else:
            # remove item if quantity submitted is zero
            del[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
    else:
        # if there's no size remove item
        if quantity > 0:
            bag[item_id] = quantity
        else:
            bag.pop(item_id)

    # overwrite session with updated variable
    request.session['bag'] = bag
    # redirect back to the view bag url
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove item from shopping bag and allow users to remove
    items directly without setting quantity to zero"""

    try:
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        # get bag variable if it exists or create one if not
        bag = request.session.get('bag', {})

        if size:
            # remove only specific size requested from dictionary
            del bag[item_id]['items_by_size'][size]
            # if size is only item in dictionary, delete item id as dictionary is now empty
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
        else:
            # if there's no size, remove (pop) from bag
            bag.pop(item_id)

        # overwrite session with updated variable
        request.session['bag'] = bag
        # imply item was successfully removed
        return HttpResponse(status=200)
    # return error to template
    except Exception as e:
        return HttpResponse(status=500)
