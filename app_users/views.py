from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.core.exceptions import ObjectDoesNotExist

from app_users.models import User
from app_users.forms import UserRegisterForm, RecoverPasswordForm
from app_users.helpers import get_random_code, user_set_random_password

from config import settings


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('Index')

    def form_valid(self, form):

        if form.is_valid():
            new_form = form.save()
            new_form.verify_code = get_random_code()

            send_mail(
                'Завершение регистрации',
                f'Добро пожаловать {new_form.email}! \n'
                f'Для окончания регистрации пройдите по ссылке:\n'
                f'http://localhost:8000/verify/{new_form.verify_code}',
                settings.EMAIL_HOST_USER,
                [new_form.email]
            )
            new_form.save()
        return super().form_valid(form)


def verify_view(request, code):
    print('='*100, type(code))
    user = User.objects.get(verify_code=str(code))
    user.is_active = True
    user.verify_code = 'NULL'
    user.save()

    return redirect('login')


def forget_email_view(request):
    if request.method == 'POST':
        recover_form = RecoverPasswordForm(request.POST)
        if recover_form.is_valid():
            email = recover_form.cleaned_data['email']
            try:
                user = User.objects.get(email=email)
                user_set_random_password(user)

                return redirect('recover_password')
            except ObjectDoesNotExist:
                form = RecoverPasswordForm()
                context = {'form': form,
                           'user_does_not_exists': recover_form.cleaned_data['email']}
                return render(request, 'users/forget_email.html', context=context)

    else:
        form = RecoverPasswordForm()
        context = {'form': form}
        return render(request, 'users/forget_email.html', context=context)


def recover_password_confirmation_view(request):
    return render(request, 'users/recover_password_confirmation.html')
