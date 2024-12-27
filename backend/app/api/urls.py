from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.countries.views import CountriesViewSet

router = DefaultRouter()
router.register(r'countries', CountriesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
