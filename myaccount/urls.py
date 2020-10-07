from django.urls import path, include
from .views import HomeView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(HomeView.as_view()), name='home'),
]