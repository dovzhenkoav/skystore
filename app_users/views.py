from django.urls import reverse_lazy
from django.views.generic import CreateView
from app_users.models import User
from app_users.forms import UserRegisterForm


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')
