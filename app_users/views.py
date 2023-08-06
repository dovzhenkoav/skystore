from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import CreateView
from app_users.models import User
from app_users.forms import UserRegisterForm

from config import settings


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')


