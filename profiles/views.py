from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Order


def profile(request):
    """ display user's profile """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        # create a new instance of user profile form using post data
        form = UserProfileForm(request.POST, instance=profile)
        # if form is valid, save and display success message
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            # if form not valid, display message to user
            messages.error(request, 'Update failed. Please ensure the form \
                           is valid.')
    else:
        # replace form with user's updated profile
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


def order_history(request, order_number):
    """ order history with order number as parameter """
    order = get_object_or_404(Order, order_number=order_number)
    # display info message to user
    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        # to check if called from order_history view
        'from_profile': True,
    }

    return render(request, template, context)
