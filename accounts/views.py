from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.

def profile (request, slug):
    pro = get_object_or_404(Profile, slug = slug)
    context = {
        'profile': pro,
    }
    return render(request, 'pages/profile.html', context)