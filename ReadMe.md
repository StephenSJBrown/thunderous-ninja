# thunderous ninja

## intructions to set up server for the first time

1. Navigate to the directory you want to create the repo in (without using mkdir to create a new folder)
2. run `git clone <url to repo>`
3. navigate into repo `cd thunderous-ninja`
4. Create a new environment with Python3.7 using `conda create -n <environment name> python=3.7`
5. pip install all requirements `pip install -r requirements.txt`


## To add seed data to database:

### If db already exists, first do this

`dropdb <your-db-name>`

### After

`createdb <your-db-name>`
`python migrate.py`
`flask seed`

## Finally, to get the server up and running

`flask run`
