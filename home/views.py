from django.shortcuts import render


def index(request):
    """ return home page """
    return render(request, 'home/index.html')


def contact_us(request):
    """ return 'contact_us' page """
    return render(request, 'info/contact_us.html')


def what_is_a_mtb(request):
    """ return 'what is a mountain bike?' page """
    return render(request, 'buying_guides/what_is_a_mtb.html')
