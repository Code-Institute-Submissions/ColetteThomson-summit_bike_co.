from django.shortcuts import render


def profile(request):
    """ display the user's profile """

    # return a profile.html with empty context
    template = 'profiles/profile.html'
    context = {}

    return render(request, template, context)
