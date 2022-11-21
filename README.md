# shopcloud-django-monitoring

Monitoring App

## QUickstart

1. Add "polls" to your INSTALLED_APPS setting like this::

```py
INSTALLED_APPS = [
    ...
    'polls',
]
```

2. Include the polls URLconf in your project urls.py like this::

```
path('polls/', include('polls.urls')),
```

3. Run `python manage.py migrate` to create the polls models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a poll (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/monitoring/ to participate in the poll.

codecov tox tox-py