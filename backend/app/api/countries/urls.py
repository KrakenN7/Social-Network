from django.urls import path

import api.countries.views

urlpatterns = [
    path(
        "",
        api.countries.views.CountriesListApiView.as_view(),
        name="countries",
    ),
]
