# Coding Assesment
### Create, activate the virtual env and install required packages:

`pip install -r requirements.txt`

Configure the postgresql database on local machine.

or try on docker

    `docker run --name postgres -e POSTGRES_HOST_AUTH_METHOD=trust -e POSTGRES_DB=postgres -p 5432:5432 postgres`

### Unit test and integration test with PyTest

`pytest -v`

### Migrate the database
`python manage.py makemigrations`

`python manage.py migrate`

**now import the sample data to postgresql database that was provided with question. sql or csv data**

### Run the server
`python manage.py runserver`

### API gateway - Swagger 

`https://127.0.0.1:8000/swagger/`

### Documentation - Redoc

`https://127.0.0.1:8000/redoc/`

