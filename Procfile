release: python manage.py migrate
release: python manage.py makemigrations

web: gunicorn   myestate.wsgi --log-file -

