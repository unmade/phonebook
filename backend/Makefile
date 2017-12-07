runserver:
	python phonebook/manage.py runserver --settings=phonebook.settings.local

test:
	python phonebook/manage.py test phonebook --settings=phonebook.settings.local

lint:
	pylint phonebook/* --rcfile=.pylintrc --disable=C0111 --load-plugins=pylint_django