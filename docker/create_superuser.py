from django.contrib.auth.models import User


username = 'admin'
email = 'strausd@me.com'
password = 'admin'

if User.objects.filter(username=username).count() == 0:
    User.objects.create_superuser(username, email, password)
    print('Created superuser')
    print('Username: ' + username)
    print('Password: ' + password)
else:
    print('Superuser already exists')
