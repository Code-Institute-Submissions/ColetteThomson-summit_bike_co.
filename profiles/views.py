from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm


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
