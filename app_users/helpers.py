import random

from django.core.mail import send_mail

from app_users.models import User
from config import settings


def get_random_code():
    code = int(f'{random.randint(1, 9)}{random.randint(1, 9)}{random.randint(1, 9)}{random.randint(1, 9)}')
    return code


def user_set_random_password(user: User):
    code = get_random_code()
    user.set_password(str(code))
    user.save()

    send_mail(
        'Завершение регистрации',
        f'Изменение пароля для {user.email}! \n'
        f'Новый код для входа: {code}',
        settings.EMAIL_HOST_USER,
        [user.email]
    )

