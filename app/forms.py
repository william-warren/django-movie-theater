from django import forms

class NewTicketForm(forms.Form):
    name = forms.CharField()
    showing_id = forms.IntegerField()