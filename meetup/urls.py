from django.urls import path
from . import views

app_name = "meetup"
urlpatterns = [
    path("meetups/", views.index, name="index"),
    path("meetups/<slug:meetup_slug>", views.meetup_detail, name="meetup_detail"),
]
