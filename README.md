# LibraryAPI

### Developed API project focuses mostly on exploring Django / DRF capabilities.
 - however there were other than Django / DRF reviewed, especially in terms of dev env and testing
```
Project was developed as below:

Phase 1. Developing CRUD functions in Django / DRF
 - mixing Models, Serializers, builtin DRF Class-based views, Routers
 - and following typical DRF setup ended creating a few CRUD apis really fast
 - from testing pov there was pytest-django lib explored
 - apart of that quite complex dev env was used with: precommit, mypy (doesnt work well with DRF), shell_plus and even tools for class diagram generation (based on Django models)

Phase 2. Integration of drf-spectacular, looking into documentation options
 - as per documentation drf-spectacular integration provided powerful than satisfied solution giving three types of documentation
 - JSON OpenAPI Schema (raw JSON OpenAPI), Swagger, ReDoc,

Phase 3. Exploring different Authentication options
 - three ways of User Authentication were implemented / reviewed
 - SessionAuthentication -> TokenAuthentication -> JWTAuthentication
 - SessionAuthentication-branch and TokenAuthentication-branch are backuped branches for those previous solutions
 - JWTAuthentication is final solution (GET token/ request should be used for token fetching)
 - in terms of Authorization in this stage there is basic IsAuthenticated mode setuped via settings.py

Phase 4. Exploring Authorization approaches
 - setuping some endpoints to be Admin available only
 - using custom Permission rule based on BasePermission class
 - understanding other options in terms of Authorizations (mainly DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly)

Phase 5. Exploring/integrating default DRF Filtering / Sorting / Pagination capabilities
 - it was amazingly small task to setup Filtering and Pagination to books/ endpoints
 - the same is about sorting (omitted), but it was done with queryset definition

Phase 6. Implementing custom Exception handler in DRF

Phase 7. Exploring writing custom Middleware w Django/DRF
```



### SETUP STEPS:
```
Initial project setup:
 - git clone git@github.com:DanielPalacz/LibraryAPI.git
 - python -m venv venv
 - source venv/bin/activate
 - pip install -r requirements.txt
 - python manage.py makemigrations
 - python manage.py migrate
 - python manage.py createsuperuser

Populate minimum of examples to DB:
 - PYTHONPATH=. python tests/populate_db.py

Setup statics / api schema:
 - python manage.py collectstatic
 - python manage.py spectacular --file schema.yml

For now API is not available publicly.
 - python manage.py runserver
```


### USAGE:
```
Documentation enpoints:
 - http://127.0.0.1:8000/
 - http://127.0.0.1:8000/api/schema/
 - http://127.0.0.1:8000/api/schema/swagger-ui/
 - http://127.0.0.1:8000/api/redoc/

For start play with Swagg

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

### NOTES / WORK TRACKER TABLE

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
| integrating different Authentication approaches       | feature  | [DONE]        |
| Automation Testing (test coverage for Authentication) | testing  | [NOT STARTED] |
| Manual testing (curl, Postman)                        | testing  | [IN PROGRESS] |
| exploring builtin Permission mechanisms               | testing  | [DONE]        |


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
1. Run tests without Authentication-Authorization features:
- FORCE_NO_AUTH=true DJANGO_SETTINGS_MODULE=LibraryProject.settings PYTHONPATH=. pytest -vv tests/
- FORCE_NO_AUTH=true DJANGO_SETTINGS_MODULE=LibraryProject.settings PYTHONPATH=. pytest -vv tests/ -m "not authorization"
- FORCE_NO_AUTH=true DJANGO_SETTINGS_MODULE=LibraryProject.settings PYTHONPATH=. pytest  -vv --cov-report=html:TestCoverageReport tests/
or set env vars explicitly:
export DJANGO_SETTINGS_MODULE="LibraryProject.settings"
export FORCE_NO_AUTH=true

2. Run tests with Authentication-Authorization features:
- FORCE_NO_AUTH=false DJANGO_SETTINGS_MODULE=LibraryProject.settings PYTHONPATH=. pytest -vv tests/ -m authorization
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
 - checking Django authorization/authentication builtins (views, login_required decorator)
 - checking JWT tokens (djangorestframework-simplejwt)
 - checking how to implement different roles in Django, is there something like Custom Permissions?

[NOT DONE]
 - manual testing - playing with Postman
 - GitHubActions / Heroku Deployment - to consider

```

---
---

## Authentication and Authorization in Django/DRF
```
1. Authentication
    a) BasicAuthentication, password-based Authentication
    b) Login-Based Authentication (SessionAuthentication)
    c) Token-Based Authentication (Simple version from DRF: TokenAuthentication)
    d) Token-Based Authentication (JWT token authorization)
    e) OAuth2/OpenID Connect

2. Authorization
    a) Django's login_required Decorator (dedicated for Session-based typical Frontend Web APP, no good for APIs)
    b) DRF builtin permission classes (AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly)
    c) DjangoModelPermissions
    d) DjangoObjectPermissions (extends DjangoModelPermissions, additional lib needed like: django-guardian)
    e) Customized Role-Based Access Control (RBAC) solution
```
 - [More details about Authorization (Permission Mechanisms in Django and DRF)](./README_AUTHORIZATION_MECHANISMS.md)

### Authentication/Authorization in Django/DRF - APPROACH 1
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

### Authentication/Authorization in Django/DRF - APPROACH 2
- Authentication: TokenAuthentication (setup via settings.py)
- Authorization: IsAuthenticated (setup via settings.py)
- two endpoints have override Authorization mode to AllowAny (/, login/)
```
- adding 'rest_framework.authtoken' to INSTALLED_APPS
- python manage.py migrate
- update settings.DEFAULT_AUTHENTICATION_CLASSES

1)
 - use login endpoint to get token value and load into Swagger or prepare curl requests
 - use logout endpoint for token deactivation
2)
curl request example:

curl -X 'GET' \
  'http://127.0.0.1:8000/authors/' \
  -H 'accept: application/json' \
  -H 'Authorization: Token 9105517aa58df364a5b9f9eeab978e34b07739da'
```

### Authentication/Authorization in Django/DRF - APPROACH 3
- Authentication: JWTAuthentication (setup via settings.py)
- Authorization: IsAuthenticated (setup via settings.py)
- one endpoint has override Authorization mode to AllowAny (/)
```
- pip install djangorestframework-simplejwt
- adding 'rest_framework_simplejwt' to INSTALLED_APPS
- update settings.DEFAULT_AUTHENTICATION_CLASSES

1)
 - use token/ and token/refresh/ endpoints to fetch token data
2)
curl request example:

curl -X 'GET' \
  'http://127.0.0.1:8000/books/' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer BEARER_TOKEN'
```


### Authentication/Authorization in Django/DRF - APPROACH 4
- Authentication: JWTAuthentication (setup via settings.py)
- Authorization: IsAuthenticated (setup via settings.py)
  * users/ endpoints have manually assigned builtin IsAdminUser Permission rule
  * register/ endpoint has manually assigned custom IsEmployee Permission rule (based on BasePermission class)
  * one endpoint has override Authorization mode to AllowAny (/)
```
For now it is enough. There is many options in terms of Authorization (Permission) support in Django / DRF.
There is quite many builtin / around-builtin solution in terms of Authorization (in Django/DRF)
But next to consider would be  related to Django builtin Permission system: DjangoModelPermissions and later DjangoObjectPermissions.
Both are more suitable for typical Frontend/Backend application when APIs will be often less demanding for Authorization systems. Worth to know that DjangoModelPermissions is really fast in terms of Development.
```
