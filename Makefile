install:
	pip install --upgrade pip --no-cache &&\
		pip install -r requirements.txt\
			pip install -r opt-requirements.txt
install-required:
	pip install --upgrade pip --no-cache &&\
		pip install -r requirements.txt
migrations:
	python manage.py makemigrations &&\
		python manage.py migrate
format:
	black *.py */*.py
lint:
	pylint --disable=R,C --ignore=static --ignore=templates */
run:
	python manage.py runserver
