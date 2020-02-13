# thunderous ninja

## intructions to set up server for the first time

1. Navigate to the directory you want to create the repo in (without using mkdir to create a new folder)
2. run `git clone <url to repo>`
3. navigate into repo `cd thunderous-ninja`
4. Create a new environment with Python3.7 using `conda create -n <environment name> python=3.7`
5. pip install all requirements `pip install -r requirements.txt`
6. create .env file your root directory with the following codes.
`FLASK_APP='start'`
`FLASK_ENV='development'`
`DATABASE_URL='postgres://localhost:5432/<your-db-name>'`
`SECRET_KEY= os.urandom(32)`
`DB_TIMEOUT=300`
`DB_POOL=5`


## To add seed data to database:

### If db already exists, first do this

`dropdb <your-db-name>`

### After

Create the database `createdb <your-db-name>`

Add the tables based on the models in the file `python migrate.py`

Run the seed file to populate the tables `flask seed`

## Finally, to get the server up and running

`flask run`
