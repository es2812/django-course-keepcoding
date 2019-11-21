# django-course-keepcoding
General repository for code used in the keepcoding.io course: Django + Python &amp; REST

This tutorial works with Python 2.6 and Django 1.9. Changes have been made in some instances to adapt the code to Python 3 and Django 2.2. They are the following:

- Section 6:
  - URLs on frikr/urls.py are defined using the method `path`, instead of `url`, and using a normal string instead of a regex. 
  - The function associated with an url has to be called after importing its containing module (`views.py`), instead of being written down as a string.
- Section 7:
  - To change the way a model's instance is displayed in the admin page, the `__str__` method is used instead of `__unicode__`.
- Section 10:
  - Since Django 2.0 the ForeignKey constructor requires an additional attribute, `on_delete`.
  - With Python 3 django no longer complains when given an UTF-8 character.