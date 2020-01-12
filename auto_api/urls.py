from django.urls import path, include
from rest_framework import routers
from auto_api.factories import ViewSetFactory

router = routers.DefaultRouter()
viewsets = ViewSetFactory.get_viewsets()

for viewset in viewsets:
    router.register(f'{viewset.lower()}s', viewsets[viewset])

app_name = 'auto_api'
urlpatterns = [
    path('', include(router.urls))
]
