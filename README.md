# workout-personal-project



## Set Up

```py
# create a virtual environment:
mkvirutualenv <NAME>

# install requirements:
pip install -r requirements.txt

# set up database:
createdb workouts
python manage.py db upgrade
python seed.py

# start server:
python app.py

# defaults to port 5000
# http://localhost:5000/
```

## Technology Used

### Languages
* Javascript
* Python
* SQL

### Libraries
* Jquery

### Frameworks
* Flask
    * flask_login
    * flask_modus
    * flask_wtf
    * flask_bcrypt
    * flask_sqlalchemy

### Database
* Postgres
