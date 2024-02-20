from django.urls import path
from . import views

app_name = "meetup"
urlpatterns = [
    path("", views.index, name="index"),
    path("<slug:meetup_slug>/success", views.successView, name="success"),
    path("<slug:meetup_slug>", views.meetup_detail, name="meetup_detail"),
]
