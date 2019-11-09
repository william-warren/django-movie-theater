from django.core.management.base import BaseCommand, CommandError
from app import models

MOVIES = {
    "Avengers Endgame": {
        "title": "Avengers Endgame",
        "rating": "PG-13",
        "genre": "Sci-Fi",
        "runtime": "3hr2m",
        "showtimes": ["1:00 PM", "3:30 PM", "5:00 PM", "7:30 PM", "9:00 PM"],
    },
    "Avengers Infinity War": {
        "title": "Avengers Infinity War",
        "rating": "PG-13",
        "genre": "Sci-Fi",
        "runtime": "2hr40m",
        "showtimes": ["12:15 PM", "2:15 PM", "4:15 PM", "6:15 PM", "8:15 PM"],
    },
    "Avengers Age of Ultron": {
        "title": "Avengers Age of Ultron",
        "rating": "PG-13",
        "genre": "Sci-Fi",
        "runtime": "2hr22m",
        "showtimes": ["2:45 PM", "5:45 PM", "7:45 PM", "9:45 PM"],
    },
    "The Avengers": {
        "title": "The Avengers",
        "rating": "PG-13",
        "genre": "Sci-Fi",
        "runtime": "2hr23m",
        "showtimes": ["11:00 AM", "1:00 PM", "3:00 PM", "11:00 PM"],
    },
}


class Command(BaseCommand):
    help = "Seeds the database with movies based on the movie theater python benchmark"

    def handle(self, *args, **options):
        for movie in MOVIES.values():
            self.create_movie(movie)

    def create_movie(self, movie_data: dict):
        showtimes = movie_data.pop("showtimes")
        title = movie_data.pop("title")
        movie, created = models.Movie.objects.get_or_create(
            title=title, defaults=movie_data
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f"{title} created"))
        else:
            self.stdout.write(f"{title} already exists")

        for showtime in showtimes:
            showing, created = movie.showing_set.get_or_create(showtime=showtime)
            if created:
                self.stdout.write(self.style.SUCCESS(f"{title} @ {showtime} created"))
            else:
                self.stdout.write(f"{title} @ {showtime} already exists")
