release: python manage.py makemigrations && python manage.py migrate
web: gunicorn coachAPI.wsgi:application --log-file -