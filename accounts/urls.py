from django.urls import path, include
from . import views


app_name = 'accounts'

urlpatterns = [
    path('profile/', views.UserProfile, name="user-profile"),
    path('profile/<str:slug>', views.profile, name="profile"),
    path('', include('django.contrib.auth.urls')),
]
