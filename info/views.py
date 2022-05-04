from django.shortcuts import render


def who_we_are(request):
    """ return 'who we are' page """
    return render(request, 'info/who_we_are.html')


def cycle_to_work(request):
    """ return 'cycle to work scheme' page """
    return render(request, 'info/cycle_to_work.html')


def terms_conditions(request):
    """ return 'terms and conditions' page """
    return render(request, 'info/terms_conditions.html')
