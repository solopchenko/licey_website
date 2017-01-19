from django.shortcuts import render
from django.views import View
from django.shortcuts import get_object_or_404

from .models import Person

# Create your views here.
class PersonView(View):
    def get(self, request, username, *args, **kwargs):
        person = get_object_or_404(Person, id=username)
        return render(request, 'person.html', {'person': person})
