PROJECT_NAME = phonebook


runserver:
	python $(PROJECT_NAME)/manage.py runserver --settings=$(PROJECT_NAME).settings.local

test:
	pytest $(PROJECT_NAME)

lint:
	pylint $(PROJECT_NAME)/*

isort:
	isort -r $(PROJECT_NAME)
