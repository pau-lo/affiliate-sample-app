from django.shortcuts import render


def home(request):
    return render(request, 'affiliate/home.html')
