from django.contrib import admin
from app.models import Ticket, Showing, Movie

# Register your models here.
admin.site.register(Ticket)
admin.site.register(Showing)
admin.site.register(Movie)
