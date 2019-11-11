from django.shortcuts import render, redirect
from app.models import Movie, Ticket, Showing
from app.forms import NewTicketForm
from django.views import View

# Create your views here.
def home(request):
    movies = Movie.objects.all()
    return render(request, "home.html", {"movies": movies})


class NewTicket(View):
    def get(self, request, id):
        movie = Movie.objects.get(id=id)
        form = NewTicketForm()
        return render(request, "new_ticket.html", {"movie": movie, "form": form})

    def post(self, request, id):
        form = NewTicketForm(request.POST)
        if form.is_valid():
            show_id = request.POST["showing_id"]
            showing = Showing.objects.get(id=show_id)
            ticket = Ticket.objects.create(
                name=request.POST["name"], 
                showing=showing
            )
            return redirect("ticket_detail", ticket.id)
        else:
            movie = Movie.objects.get(id=id)
            form = NewTicketForm()
            return render(request, "new_ticket.html", {"movie": movie, "form": form})


def ticket_detail(request, id):
    ticket = Ticket.objects.get(id=id)
    return render(request, "ticket_detail.html", {"ticket": ticket})

