# LibraryAPI

### Library API system 'business logic' requirements:
```
Deliver API solution handling such cases:
- adding book item to specific category in the system
- displaying all categories from the system
- displaying all authors from the system
- displaying all books from the given category
- displaying all books writen by then given Autor
- editing previously added book item
- removing book item completely

Provide sufficient Authentication/Authorization.
Deliver decent, clear documentation.
```

# Work progress

| Item                                                 | Comment | Status        |
|------------------------------------------------------|---------|---------------|
| Django/DRF initial project setup                     | -       | [DONE]        |
| shell plus setup                                     | -       | [DONE]        |
| precommit/mypy  setup                                | -       | [DONE]        |
| Models creation                                      | -       | [DONE]        |
| Auto-generating diagram class                        | -       | [DONE]        |
| Automation Testing / Playing with pytest-django      | -       | [IN PROGRESS] |
| DRF Serializers (errors, validations)                | -       | [DONE]        |
| Views, builtin DRF views                             | -       | [DONE]        |
| DRF Routers                                          | -       | [DONE]        |
| Manual testing (curl, Postman)                       | -       | [IN PROGRESS] |
| coverage package for test coverage metrics           | -       | [DONE]        |
| drf_spectacular package integration (Swagger, Redoc) | -       | [DONE]        |
| displaying all categories from the system            | [F]     | [DONE]        |
| adding book item to specific category in the system  | [F]     | [DONE]        |
| displaying all books from the given category         | [F]     | [DONE]        |
| displaying all books writen by then given Author     | [F]     | [DONE]        |
| editing previously added book item                   | [F]     | [DONE]        |
| removing book item completely                        | [F]     | [DONE]        |
| displaying all authors from the system               | [F]     | [DONE]        |



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
 - installing: pytest, pytest-django, coverage
 - preparing 'pytest.ini' file
 - creating fixture for dynamically creating Database setup
  --- adding specific 'test' settings.py file where sqlite3 is 'in memory' mode
- live_server awesome builtin fixture
- coverage package integration - for test coverage metrics (files: pytest.ini, .coveragerc)

USAGE:
- PYTHONPATH=. pytest -vv tests/
- PYTHONPATH=. pytest -s -vv tests/
- PYTHONPATH=. pytest -vv --cov-report=html:TestCoverageReport tests/
```


# DRF notes

```
DRF components:
 - Serializers
 - Views, also builtin views (viewset, APIView, etc)
 - Routers, like: DefaultRouter
 - Typical Django Url-linking approach

Thoughts:
 - DRF works bad with mypy, there is no specific stubs extension    [Minuse]
 - automates a lot, one can realy fast deliver complex api       [Posisitive]
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
    b) Login-Based Authentication (Session)
    c) Token-Based Authentication
    d) OAuth2/OpenID Connect

2. Authorization
    a) Permissions in DRF
    b) Django's login_required Decorator
    c) Role-Based Access Control (RBAC)
```
