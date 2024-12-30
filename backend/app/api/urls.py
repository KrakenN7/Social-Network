from django.urls import path, include

urlpatterns = [
    path("countries/", include("api.countries.urls")),
    path("ping/", include("api.ping.urls")),
]
