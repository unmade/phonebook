# Phonebook

![Travis CI](https://travis-ci.org/unmade/phonebook.svg?branch=master)
[![Coverage Status](https://coveralls.io/repos/github/unmade/phonebook/badge.svg?branch=coveralls)](https://coveralls.io/github/unmade/phonebook?branch=coveralls)

![Main page image](https://raw.githubusercontent.com/unmade/phonebook/master/docs/images/1%20main.png "Main page")

This is just simple phonebook to store employees contacts.
See how it [looks](docs/LOOK.md)


## QuickStart

Simply run:
```
docker-compose up --build
```

Create superuser for django admin:
```
docker-compose run web python3 phonebook/manage.py createsuperuser
```

> Don't forget to change password and security settings in [secrets](secrets/)


## Development

Just run:
```
docker-compose -f docker-compose.yml -f docker-compose.local.yml up --build
```

> You could set up settings suitable for development in `.env` file


## Testing

To run test locally:
```
docker-compose -f docker-compose.yml -f docker-compose.test.yml up test
```
