from django.shortcuts import render


def what_is_a_mtb(request):
    """ return 'what is a mountain bike?' page """
    return render(request, 'buying_guides/what_is_a_mtb.html')


def mtb_sizing(request):
    """ return 'mountain bike sizing guide' page """
    return render(request, 'buying_guides/mtb_sizing.html')
