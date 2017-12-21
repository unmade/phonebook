PROJECT_NAME = phonebook


collectstatic:
	python $(PROJECT_NAME)/manage.py collectstatic --settings=$(PROJECT_NAME).settings.local

front:
	cd ../frontend && gulp && cd -

isort:
	isort -r $(PROJECT_NAME)

lint:
	pylint $(PROJECT_NAME)/*

runserver:
	python $(PROJECT_NAME)/manage.py runserver --settings=$(PROJECT_NAME).settings.local

test:
	pytest $$(pwd)/$(PROJECT_NAME)
