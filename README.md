# django-course-keepcoding
General repository for code used in the keepcoding.io course: Django + Python &amp; REST

This tutorial works with Python 2.6, Django 1.9 and Django REST Framework 3.1.3. Changes have been made in some instances to adapt the code to Python 3, Django 2.2 and Django REST Framework 3.3.3. They are the following:

- Section 6:
  - URLs on frikr/urls.py are defined using the method `path`, instead of `url`, and using a normal string instead of a regex. 
  - The function associated with an url has to be called after importing its containing module (`views.py`), instead of being written down as a string.
- Section 7:
  - To change the way a model's instance is displayed in the admin page, the `__str__` method is used instead of `__unicode__`.
- Section 10:
  - Since Django 2.0 the ForeignKey constructor requires an additional attribute, `on_delete`.
  - With Python 3 django no longer complains when given an UTF-8 character.
  - The syntax `<int:var>` can be used in the path method to recognize integers instead of using regex.
- Section 11:
  - Since Django 2.0 the `User.is_authenticated` property cannot be called as a method.
- Section 12:
  - In Python 3 the `super` method call doesn't require the object or self attributes.
  - In Python 3 `UnicodeDecodeError` is not thrown anymore with an UTF-8 character.
- Section 17:
  - In Django 2.2 the `static` tag must be loaded in the template before allowing usage.
- Section 22:
  - Since Django REST Framework 3.3.0 creating a `ModelSerializer` without a `fields` or `exclude` attribute is disallowed.
- Section 27:
  - Since Django REST Framework 3.9.0 `Router.register` method's argument `base_name` is deprecated in favour of `basename`.