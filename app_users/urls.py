from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from app_users.views import RegisterView, verify_view



urlpatterns = [
    path('login', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('verify/<int:code>', verify_view, name='verify'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    # path('profile/', ProfileView.as_view(), name='profile'),

]
