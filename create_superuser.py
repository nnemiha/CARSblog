import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cinema_backend.settings')
django.setup()

from django.contrib.auth import get_user_model
User = get_user_model()

def create_superuser():
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='123'
        )
        print('Суперпользователь создан успешно')
    else:
        print('Суперпользователь уже существует')

if __name__ == '__main__':
    create_superuser() 