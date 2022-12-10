# pytest_django_crud
To demonstrate pytest for django rest framework
## How to run project?

* Clone this repository.
* Create virtualenv with Python 3.
* Install dependences.
* Run the migrations.

```
git clone https://github.com/naveenreddymanukonda/pytest_django_crud.git
cd pytest_django_crud
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
pytest
```