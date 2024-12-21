from django.urls import path

from ping import views

urlpatterns = [
    path("", views.PingApiView.as_view(), name="ping"),
]
