from django.shortcuts import render, redirect


def view_bag(request):
    """ view products in shopping bag """
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ add product quantity to shopping bag """
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

    # overwrite session with updated variable
    request.session['bag'] = bag
    # redirect user back to their original page
    return redirect(redirect_url)
