# Coding Assesment
Configure the postgresql database on local machine.

or try on docker

    `docker run --name postgres -e POSTGRES_HOST_AUTH_METHOD=trust -e POSTGRES_DB=postgres -p 5432:5432 postgres`

### Unit test and integration test with PyTest

`pytest -v`

now import the sample data that was provided with question. sql or csv data

`python manage.py makemigrations`

`python manage.py migrate`

### Run the server
`python manage.py runserver`

### API gateway - Swagger 

`https://127.0.0.1:8000/swagger/`

### Documentation - Redoc



`https://127.0.0.1:8000/redoc/`

