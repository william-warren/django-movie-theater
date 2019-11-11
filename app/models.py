from django.db import models

# Create your models here.
class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField()
    rating = models.TextField()
    genre = models.TextField()
    runtime = models.TextField()


class Showing(models.Model):
    id = models.AutoField(primary_key=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    showtime = models.TimeField()


class Ticket(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    purchased_at = models.DateTimeField(auto_now=True)
    showing = models.ForeignKey(Showing, on_delete=models.PROTECT)
