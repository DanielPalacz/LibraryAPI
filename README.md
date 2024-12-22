# LibraryAPI


### SETUP STEPS:
```
git clone git@github.com:DanielPalacz/LibraryAPI.git
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

Populate minimum of examples to DB:
PYTHONPATH=. python tests/populate_db.py

```


### USAGE:
```
python manage.py runserver
http://127.0.0.1:8000/
http://127.0.0.1:8000/api/schema/swagger-ui/
http://127.0.0.1:8000/api/redoc/
```


### Business logic / requirements:
```
Deliver API solution handling such cases:
- adding book item to specific category in the system
- displaying all categories from the system
- displaying all authors from the system
- displaying all books from the given category
- displaying all books writen by then given Autor
- editing previously added book item
- removing book item completely

Provide sufficient Authentication/Authorization approach.
Deliver decent, clear documentation.
```

---

## DIFFERENT PROJECT NOTES

### NOTES / WORK TRACKER

| Item                                                  | Comment  | Status        |
|-------------------------------------------------------|----------|---------------|
| Django/DRF initial project setup                      | setup    | [DONE]        |
| shell plus setup                                      | setup    | [DONE]        |
| precommit/mypy  setup                                 | learning | [DONE]        |
| Models creation                                       | setup    | [DONE]        |
| Auto-generating diagram class                         | learning | [DONE]        |
| DRF Serializers (errors, validations)                 | learning | [DONE]        |
| Views, builtin DRF views                              | learning | [DONE]        |
| DRF Routers                                           | learning | [DONE]        |
| coverage package for test coverage metrics            | testing  | [DONE]        |
| drf_spectacular package integration (Swagger, Redoc)  | setup    | [DONE]        |
| displaying all categories from the system             | feature  | [DONE]        |
| adding book item to specific category in the system   | feature  | [DONE]        |
| displaying all books from the given category          | feature  | [DONE]        |
| displaying all books writen by then given Author      | feature  | [DONE]        |
| editing previously added book item                    | feature  | [DONE]        |
| removing book item completely                         | feature  | [DONE]        |
| displaying all authors from the system                | feature  | [DONE]        |
| Automation Testing / Playing with pytest-django       | testing  | [DONE]        |
| Automation Testing (test coverage for Authentication) | testing  | [NOT STARTED] |
| Manual testing (curl)                                 | testing  | [DONE]        |


#### Django Shell Plus setup
```
SETUP STEPS:
- pip install django-extensions
- pip install ipython
- add "django_extensions" to INSTALLED_APPS

USAGE:
 - python manage.py shell_plus
 - python manage.py shell_plus --ipython

BENEFITS / USE CASES?
 - it setups environment where all Django-related artefacts are already imported
 - ipython gives supporting tab feature
```

#### precommit / mypy setup
```
SETUP STEPS:
 - pip install pre-commit
 - pre-commit install
 - pip install mypy
 - pip install extended-mypy-django-plugin
 - pip install django-stubs django-stubs-ext
 - files: .pre-commit-config.yaml, mypy.ini

BENEFITS / USE CASES?
 - auto checks before commit
 - with mypy there is intensive type checking (even although Python is dynamic typed lang)
```

#### Generating model diagrams:
```
SETUP STEPS:
 - sudo apt-get install graphviz graphviz-dev
 - pip install django-extensions
 - pip install pygraphviz
 - export DJANGO_SETTINGS_MODULE=LibraryProject.settings

USAGE:
 - python manage.py graph_models library_api -o LibraryAPI_Model_diagram_class_for_dedicated_api.png
 - python manage.py graph_models -a -o LibraryAPI_Model_DiagramClass_for_all_apps.png
```

#### Testing / pytest with other supporting libs:
```
SETUP STEPS:
 - installing: pytest, pytest-django, coverage, pytest-cov
 - preparing 'pytest.ini' file
 - creating fixture for dynamically creating Database setup
  --- adding specific 'test' settings.py file where sqlite3 is 'in memory' mode
- live_server awesome builtin fixture
- coverage package integration - for test coverage metrics (files: pytest.ini, .coveragerc)

USAGE:
- PYTHONPATH=. pytest -vv tests/
- PYTHONPATH=. pytest -s -vv tests/
- PYTHONPATH=. pytest -vv --cov-report=html:TestCoverageReport tests/

Run tests without Authentication-Authorization features:
- DJANGO_SETTINGS_MODULE=tests.settings PYTHONPATH=. pytest -vv tests/
- FORCE_NO_AUTH=true DJANGO_SETTINGS_MODULE=LibraryProject.settings PYTHONPATH=. pytest -vv tests/
- and/or setup specific environment variables
```


#### Django Rest Framework notes

```
DRF components:
 - Serializers
 - Views, also builtin views (viewset, APIView, etc)
 - Routers, like: DefaultRouter
 - Typical Django Url-linking approach

Thoughts:
 - DRF works bad with mypy, there is no specific stubs extension    [Minuse]
 - automates a lot, one can really fast deliver complex api       [Posisitive]
 - drf_spectacular, gives three type of documentation setup...   [Big posisitive]
```


### Making use of DRF benefits, 'Book category' api endpoints example:
```
What was needed?
 - BookCategory model
 - BookCategorySerializer
 - DefaultRouter
 - typical Django url-linking setup
 - with minimum amount of code, but specific configuration below was the output
```

| Method    | Endpoint              | Description                                 |
|-----------|-----------------------|---------------------------------------------|
| GET	     | /categories/	         | Fetching list of all categories              |
| GET	     | /categories/<id>/	 | Fetching details about the given category    |
| POST	     | /categories/	         | Creating new category                        |
| PUT	     | /categories/<id>/	 | Full actualization of the given category     |
| PATCH	 | /categories/<id>/	 | Partial actualization of the given category  |
| DELETE    | /categories/<id>/	 | Deleting existing category                   |



#### Working/learning notes

```
[DONE ENOUGH FOR NOW]
 - practise defining models and relationships (OneToMany, ManyToMany)
 - practise creating serializers (inc: handling errors, data validations)
 - practise creating views using DRF builtins
 - checking routers potential, if it's worth using (checking default documentation that is created)
 - checking other option for API documentation (like  Swagger from drf-yasg)
 - automation testing - finding good approach for fixturing Web server handling all app


[NOT DONE]
 - checking Django authorization/authentication builtins (views, login_required decorator)
 - checking JWT tokens (djangorestframework-simplejwt)
 - checking how to implement different roles in Django, is there something like Custom Permissions?
 - manual testing - playing with Postman
 - GitHubActions / Heroku Deployment - to consider

```

## Authentication and Authorization in Django/DRF (Typical Approaches)
```
1. Authentication
    a) BasicAuthentication, password-based Authentication
    b) Login-Based Authentication (SessionAuthentication)
    c) Token-Based Authentication (JWT token authorization)
    d) OAuth2/OpenID Connect

2. Authorization
    a) DRF builtin permission classes (AllowAny, IsAuthenticated, IsAdminUser, DjangoModelPermissions)
    b) Django's login_required Decorator
    c) Role-Based Access Control (RBAC)
```


## Authentication and Authorization in Django/DRF - APPROACH_1
- Authentication: SessionAuthentication (setup via settings.py)
- Authorization: IsAuthenticated (setup via settings.py)
- two endpoints have override Authorization mode to AllowAny (/, login/)
```
1. Swagger
 - use login endpoint to load sessionid cookie into browser session
 - restart browser page (to update for example csrftoken)
 - execute requests you need

2. curl requests
2a)
    Login via 'login/' endpoint and store cookies to temp 'cookie.txt' file:
    curl -X POST http://127.0.0.1:8000/login/ -H "Content-Type: application/json" -d '{"username": USERNAME, "password": PASSWORD}' -c cookies.txt
2b)
    cat cookies.txt # copy csrftoken, it is needed for POST-like requests
2c)
    curl -X GET http://127.0.0.1:8000/authors/ -b cookies.txt
    curl -X POST -d '{"first_name": "Adam", "last_name": "Mickiewicz", "year_of_birth_date": 1798}' http://127.0.0.1:8000/authors/ -b cookies.txt -H "Content-Type: application/json" -H "X-CSRFToken: <CSRF_TOKEN_VALUE>"
2d)
    curl -X POST http://127.0.0.1:8000/logout/ -b cookies.txt -H "Content-Type: application/json" -H "X-CSRFToken: <CSRF_TOKEN_VALUE>"
```
