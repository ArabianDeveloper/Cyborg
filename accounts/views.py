from django.shortcuts import render, get_object_or_404, redirect
from .models import *

# Create your views here.

def profile (request, slug):

    pro = get_object_or_404(Profile, slug = slug)

    context = {
        'profile': pro,
    }
    return render(request, 'pages/profile.html', context)

def UserProfile (request):

    pro = get_object_or_404(Profile, slug=request.user.profile.slug)

    context = {
        'profile': pro,
    }
    return render(request, 'pages/profile.html', context)


def addfriend(request, slug):
    friend = get_object_or_404(User, username = slug)
    print(friend)
    print(request.user.profile.friends.all())
    if friend in request.user.profile.friends.all():
        request.user.profile.friends.remove(friend)
    else :
        request.user.profile.friends.add(friend)
    return redirect('streams:streams')