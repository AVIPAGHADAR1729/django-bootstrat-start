# django-bootstrap-start-app
Simple add app in Django Project Start a Django with Boostrap setup ready Project

 Install the package using :
 pip install git+https://github.com/AVIPAGHADAR1729/django-bootstrat-start.git
 
 After installation:
=====
django-bootstrap-starter
=====

Quick start
-----------

1. Add "app" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'app',
    ]

2. Include the polls URLconf in your project urls.py like this::

    path('/', include('app.urls')),

3. Run ``python manage.py migrate`` to create the polls models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a poll (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/ to participate in the site.


# Uninstall App
pip uninstall django-bootstrap-start-0.1
