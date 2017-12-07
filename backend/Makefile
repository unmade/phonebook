PROJECT_NAME = phonebook


runserver:
	python $(PROJECT_NAME)/manage.py runserver --settings=$(PROJECT_NAME).settings.local

test:
	python $(PROJECT_NAME)/manage.py test $(PROJECT_NAME) --settings=$(PROJECT_NAME).settings.local

lint:
	pylint $(PROJECT_NAME)/*

isort:
	isort -r $(PROJECT_NAME)
