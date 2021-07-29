# shawnnovel-backend

If you don't have virtualenv installed:
	pip install virtualenv

	
Then:
	virtualenv venv
	venv\Scripts\activate
	pip install -r requirements.txt
	python manage.py makemigrations
	python manage.py migrate
	python manage.py createsuperuser
	python manage.py runserver
