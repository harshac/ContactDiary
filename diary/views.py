from django.shortcuts import render_to_response
from diary.models import Phone

def view_all(request):
    contacts = Phone.objects.all()

    return render_to_response('view_contacts.html', {'contacts':contacts})
