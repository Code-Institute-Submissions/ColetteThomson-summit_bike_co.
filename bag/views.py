from django.shortcuts import render


def view_bag(request):
    """ view products in shopping bag """
    return render(request, 'bag/bag.html')
