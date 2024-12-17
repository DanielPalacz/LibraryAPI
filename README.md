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
- displaying all books from the given category
- displaying all books writen by then given Autor
- editing previously added book item
- removing book item completely
```