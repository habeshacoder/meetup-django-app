from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} {self.Address}"


class Participants(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self) -> str:
        return f"{self.email}"


# Create your models here.
class Meetup(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.FileField(upload_to="images", default="no image")
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    participants = models.ManyToManyField(Participants, blank=True, null=True)
    organizer_email = models.EmailField()
    date = models.DateField()
