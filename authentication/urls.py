from django.urls import path
from .views import RegistrationView, LoginView, VerificationView, LogoutView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('register', RegistrationView.as_view(), name='register'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('activate/<uidb64>/<token>', VerificationView.as_view(), name='activate'),
]