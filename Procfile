"web: gunicorn AlphaFusionVN.wsgi --log-file -" 
python manage.py collectstatic --noinput
manage.py migrate
release: python manage.py migrate