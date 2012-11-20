from django.http import HttpResponse
from django.shortcuts import render_to_response
from diary.models import Phone, Person

def view_all(request):
    contacts = Phone.objects.all()

    return render_to_response('view_all.html', {'contacts':contacts})

def view_contact(request, first_name):
    person = Person.objects.get(first_name = first_name)
    contact = Phone.objects.get(person  = person)

    return render_to_response('view_contact.html', {'contacts':contact, 'message':'i am here'})