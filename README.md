# Django Movie Theater

In this project, you will implement the backend for a movie theater based on
the python benchmark movie theater project. The project has 3 primary
requirements. Users must be able to:

- View the movie theater's currently available movies
- Purchase a ticket for a particular movie showing
- View their purchased ticket

To complete this project you will have to implement the URLs, Views, Models, and
Forms as described below.

I've added a command to seed the database with data based on the python benchmark
project. If your models are correct, you can run `python3 manage.py seed_movies`
to populate your database with those movies.

To check your solution, I've provided a test suite that you can run with
`python3 manage.py test`.

## Models

This application has 3 models: `Movie`, `Showing`, and `Ticket`.

### Movie

The `Movie` model has the following fields:

- `title` - the title of the movie
- `rating` - the rating of the movie
- `genre` - the genre of the movie
- `runtime` - a string describing the duration of the movie in the format (e.g. `"1h39m"`)

### Showing

The `Showing` model has the following fields:

- `movie` - the `Movie` being shown
- `showtime` - a string describing the time the of the showing (e.g. `"1:15 PM"`)

### Ticket

The `Ticket` model has the following fields:

- `name` - the name of the person buying the ticket
- `purchased_at` - the datetime that the ticket was bought
- `showing` - the `Showing` that the ticket is for

## URLs

There are 3 urls for this application:

- `""` should route to the `home` view
- `"movie/<id>/tickets/new"` should route to the `new_ticket` view
- `"ticket/<id>"` should route to the `ticket_detail` view

## Views

### Home

The `home` view should render the `"home.html"` template and provide all
`Movie`s to the context using the key `"movies"`.

### Purchase Ticket

#### GET

On `GET`, the `purchase_ticket` view should render the `"new_ticket.html"`
template and provide two values to the context: `"movie"`, and `"form"`.
`"movie"` should be the `Movie` object identified by the id provided in
the path. `"form"` should be a fresh instance of a `NewTicketForm`.

#### POST

ON `POST`, the `purchase_ticket` view should validate the `POST`ed
form data using `NewTicketForm`. If the form is valid, it should create a new
`Ticket` for the `Showing` identified by the id submitted in the form and
redirect to `ticket_detail` for the newly created ticket. If the form is not
valid, it should render `"new_ticket.html"` and provide the movie and form
to the context (just like the GET case).

### Ticket Detail

The `ticket_detail` view should render the `"ticket_detail.html"` template
and provide the `Ticket` identified by the id provided in the path to the
context using the key `"ticket"`.

## Forms

This application should use 1 form: `NewTicketForm`.

### New Ticket Form

`NewTicketForm` should validate the following fields:

- `name` - the name of the person buying the ticket
- `showing_id` - the id of the `Showing` that the ticket is for