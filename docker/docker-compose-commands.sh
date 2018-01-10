python3 manage.py migrate
python3 manage.py make_people
python3 manage.py shell < docker/create_superuser.py
python3 manage.py runserver 0.0.0.0:8000