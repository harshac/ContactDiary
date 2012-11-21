from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from diary.models import Phone, Person
from diary.new_contact_form import ContactForm
#from diary.phone_form import PhoneForm

def view_all(request):
    contacts = Phone.objects.all()

    return render_to_response('view_all.html', {'contacts':contacts})

def view_contact(request, first_name):
    person = Person.objects.get(first_name = first_name)
    contact = Phone.objects.get(person  = person)

    return render_to_response('view_contact.html', {'contacts':contact})

def add(request):
    person_form = ContactForm()
#    person_form = PhoneForm()
    return render(request, 'add.html', {'person_form' : person_form}, context_instance = RequestContext(request))
#    return render_to_response('add.html', {'person_form' : person_form}, context_instance = RequestContext(request))

def create(request):
    form = ContactForm(request.POST)

    if form.is_valid() :
        form.save()
#        return HttpResponseRedirect('/view/' + form.cleaned_data['first_name'])
        return HttpResponseRedirect('/view/')

    return render(request, 'add.html', {'person_form' : form}, context_instance = RequestContext(request))
