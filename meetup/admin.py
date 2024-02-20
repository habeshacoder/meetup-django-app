from django.contrib import admin
from .models import Meetup, Location, Participants


# Register your models here.
class MeetupAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "slug",
        "organizer_email",
        "date",
        "description",
        "location",
    ]
    list_filter = ("location",)
    prepopulated_fields = {"slug": ("title",)}


class LocationAdmin(admin.ModelAdmin):
    list_display = ["name", "Address"]
    list_filter = ("Address",)


class ParticipantsAdmin(admin.ModelAdmin):
    list_display = ["email"]


# admin.site.register(Meetup)
admin.site.register(Meetup, MeetupAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Participants, ParticipantsAdmin)
