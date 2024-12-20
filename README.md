# LibraryAPI

```
Task: Build Library system

Goals A:
 - practicing CRUD API development skills
 - improving / learning Django and DRF
 - practising defining models and relationships (OneToMany, ManyToMany)
   - OneToMany: 1 Autor => Many Books
   - ManyToMany: 1 Book <=> Many Categories, 1 Category <=> Many Books
 - practising creating serializers (inc: handling errors, data validations)
 - practising creating views using DRF builtins
 - checking routers potential, if it's worth using (checking default documentation that is created)


Goals B:
 - checking Django authorization/authentication builtins (views, login_required decorator)
 - checking JWT tokens (djangorestframework-simplejwt)
 - checking other option for API documentation (like  Swagger from drf-yasg)
 - checking how to implement different roles in Django, is there something like Custom Permissions?

Goals C:
automation testing - finding good approach for fixturing Web server handling all app
manual testing - playing with Postman
GitHubActions / Heroku Deployment - to consider

```

### Library system functionalities:
```
- adding book item to specific category in the system
- displaying all categories from the system
- displaying all authors from the system
- displaying all books from the given category
- displaying all books writen by then given Autor
- editing previously added book item
- removing book item completely
```

# Work progress

| Item                                                | Comment | Status        |
|-----------------------------------------------------|---------|---------------|
| Django/DRF initial project setup                    | -       | [DONE]        |
| shell plus setup                                    | -       | [DONE]        |
| precommit/mypy  setup                               | -       | [DONE]        |
| Models creation                                     | -       | [DONE]        |
| Auto-generating diagram class                       | -       | [DONE]        |
| Automation Testing / Playing with pytest-django     | -       | [IN PROGRESS] |
| DRF Serializers (errors, validations)               | -       | [IN PROGRESS] |
| Views, builtin DRF views                            | -       | [IN PROGRESS] |
| DRF Routers                                         | -       | [IN PROGRESS] |
| Manual testing (curl, Postman)                      | -       | [IN PROGRESS] |
| coverage package for test coverage metrics          | -       | [DONE]        |
| displaying all categories from the system           | [F]     | [DONE]        |
| adding book item to specific category in the system | [F]     | [IN PROGRESS] |
| displaying all books from the given category        | [F]     | [NOT STARTED] |
| displaying all books writen by then given Autor     | [F]     | [NOT STARTED] |
| editing previously added book item                  | [F]     | [IN PROGRESS] |
| removing book item completely                       | [F]     | [IN PROGRESS] |
| displaying all authors from the system              | [F]     | [NOT STARTED] |

#
#### Work progress, notes
```
Setuping Django ShellPlus:
- pip install django-extensions
- pip install ipython
- add "django_extensions" to INSTALLED_APPS
and using:
 - python manage.py shell_plus
 - python manage.py shell_plus --ipython


Setupping precommit and mypy:
- pre-commit install
- pip install mypy
- pip install extended-mypy-django-plugin
- pip install django-stubs django-stubs-ext
- files: .pre-commit-config.yaml, mypy.ini

pip install pre-commit
pre-commit install


Generating model diagrams:
- sudo apt-get install graphviz graphviz-dev
- pip install django-extensions
- pip install pygraphviz
- export DJANGO_SETTINGS_MODULE=LibraryProject.settings

python manage.py graph_models library_api -o LibraryAPI_Model_diagram_class_for_dedicated_api.png
python manage.py graph_models -a -o LibraryAPI_Model_DiagramClass_for_all_apps.png


Testing / Playing with pytest-django, notes:
- dynamically creating DB setup, adding specific 'test' settings.py file where sqlite3 is 'in memory' mode
- live_server awesome builtin fixture
- integrated coverage package for test coverage metrics
Running:
- PYTHONPATH=. pytest -vv tests/
- PYTHONPATH=. pytest -s -vv tests/
- PYTHONPATH=. pytest -vv --cov-report=html:TestCoverageReport tests/
```


### DRF and Serializers:
```
What are Serializers in DRF?
 - it is functionality translating data between "Python Django world" and "API formats world"
Serializers responsibilities:
 - serialization / deserialization
 - data validation

Commonly used builtin serializers:
 - serializers.ModelSerializer
 - serializers.HyperlinkedModelSerializer

Other builtin serializers:
- serializers.Serializer (not related by default with Django model)
- serializers.ListSerializer
- serializers.BaseSerializer
```


### Builtin view, viewsets.ModelViewSet
```
- with router configuration, it gives Full set of CRUD endpoints
- below 'categories' example
```

| Method    | Endpoint              | Description                                 |
|-----------|-----------------------|---------------------------------------------|
| GET	     | /categories/	         | Fetching list of all categories             |
| GET	     | /categories/<id>/	 | Fetching details about the given category   |
| POST	     | /categories/	         | Creating new category                       |
| PUT	     | /categories/<id>/	 | Full actualization of the given category    |
| PATCH	 | /categories/<id>/	 | Partial actualization of the given category |
| DELETE    | 	/categories/<id>/	 | Deleting existing category                  |
