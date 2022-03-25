from django.shortcuts import render


def index(request):
    """ return home page """
    return render(request, 'home/index.html')
