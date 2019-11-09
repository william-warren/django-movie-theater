from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from app import models


class TestUserCanViewAllMovies(TestCase):
    def test_home_page_shows_all_movies(self):
        movies = [
            models.Movie.objects.create(
                title=f"Big Franchise Movie {i}",
                rating="PG-13",
                genre="Action",
                runtime="2h3m",
            )
            for i in range(5)
        ]

        response = self.client.get(reverse("home"))

        for book in movies:
            self.assertContains(response, book.title)


class TestUserCanPurchaseATicket(TestCase):
    def test_home_page_has_links_to_purchase_page(self):
        movies = [
            models.Movie.objects.create(
                title=f"Big Franchise Movie {i}",
                rating="PG-13",
                genre="Action",
                runtime="2h3m",
            )
            for i in range(5)
        ]

        response = self.client.get(reverse("home"))

        for movie in movies:
            link_to_buy_ticket = reverse("new_ticket", args=[movie.id])
            self.assertContains(response, link_to_buy_ticket)

    def test_GETting_new_ticket_page_renders_form_for_new_ticket(self):
        movie = models.Movie.objects.create(
            title="Big Franchise Movie", rating="PG-13", genre="Action", runtime="2h3m",
        )

        response = self.client.get(reverse("new_ticket", args=[movie.id]))

        self.assertContains(response, movie.title)
        self.assertContains(response, "<form")
        self.assertContains(response, "Buy Ticket")

    def test_POSTing_new_ticket_page_with_valid_data_creates_a_new_ticket(self):
        movie = models.Movie.objects.create(
            title="Big Franchise Movie", rating="PG-13", genre="Action", runtime="2h3m",
        )
        showing = movie.showing_set.create(showtime="noon")

        response = self.client.post(
            reverse("new_ticket", args=[movie.id]),
            {"name": "cool dude 9000", "showing_id": showing.id},
        )

        self.assertQuerysetEqual(
            showing.ticket_set.all(), ["cool dude 9000"], transform=lambda t: t.name
        )

    def test_POSTing_new_ticket_page_with_valid_data_redirects_to_ticket_detail(self):
        movie = models.Movie.objects.create(
            title="Big Franchise Movie", rating="PG-13", genre="Action", runtime="2h3m",
        )
        showing = movie.showing_set.create(showtime="noon")

        response = self.client.post(
            reverse("new_ticket", args=[movie.id]),
            {"name": "cool dude 9000", "showing_id": showing.id},
        )

        ticket_detail_url = reverse(
            "ticket_detail", args=[showing.ticket_set.last().id]
        )

        self.assertRedirects(response, ticket_detail_url)


class TestUserCanViewATicket(TestCase):
    def test_user_can_see_an_existing_ticket(self):
        movie = models.Movie.objects.create(
            title="Big Franchise Movie", rating="PG-13", genre="Action", runtime="2h3m",
        )
        showing = movie.showing_set.create(showtime="noon")
        ticket = showing.ticket_set.create(
            name="awesome possum", purchased_at=timezone.now()
        )

        response = self.client.get(reverse("ticket_detail", args=[ticket.id]))

        self.assertContains(response, ticket.name)
        self.assertContains(response, ticket.showing.showtime)
        self.assertContains(response, ticket.showing.movie.title)

