## **Auto API**
**Test**

`pip install -r requirements/requirements-testing.txt`
`pytest`

**Install**

`python setup.py install`

Add to your `INSTALLED_APPS` settings:

    INSTALLED_APPS = [
        ...
        'rest_framework',
        'django_filters',
        'auto_api'
    ]

Add to urls.py:

    urlpatterns = [
        ....
        path('api/v1/', include('auto_api.urls')),
    ]

**Usage**

Add any application and models, etc:
    
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.TextField()
    subscribers = models.IntegerField()

Now you can use CRUD for your models:

1. Add object

    `POST /api/v1/blogs/ {"name": "Test Blog1", "Subscribers": 100}`
2. Full update object

    `PUT /api/v1/blogs/<BLOG ID>/ {"name": "New name", "Subscribers": 101}`
3. Partial update

    `PATCH /api/v1/blogs/<BLOG ID>/ {"name": "Only New Name"}`
4. Delete object
    
    `DELETE /api/v1/blogs/<BLOG ID>/`
5. Get object
    
    `GET /api/v1/blogs/<BLOG ID>`
6. Get objects
    `GET /api/v1/blogs/<BLOG ID>/?name=my&subscribers=100&ordering=-id&limit=10`
    
   #### get params:
   
   - FIELD_NAME=VALUE - filter by field name
   - ordering=-FIELD_NAME - order by fields name(if -, then desc, else asc)
   - limit=NUM - paginate with NUM records per page