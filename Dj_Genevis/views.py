from django.http import HttpResponseRedirect, request
from django.shortcuts import get_object_or_404, render


def home_view(request):
    # View returning a home page

    return render(request, 'home.html',)
    
