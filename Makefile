install:
	pip install --upgrade pip --no-cache &&\
		pip install -r requirements.txt\
			pip install -r requirements.dev.txt
install-required:
	pip install --upgrade pip --no-cache &&\
		pip install -r requirements.txt
migrations:
	python ./app/manage.py makemigrations &&\
		python ./app/manage.py migrate
format:
	black *.py */*.py
lint:
	pylint --disable=R,C --ignore=static --ignore=templates */
run:
	python ./app/manage.py runserver
