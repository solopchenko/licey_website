from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views import View

from .models import EduProgram

# Create your views here.
class ProgramView(View):
    def get(self, request, program_slug, *args, **kwargs):
        program = get_object_or_404(EduProgram, slug=program_slug)

        context = {'program': program}

        template = 'program.html'

        return render(request, template, context)


class EducationView(View):
    def get(self, request, *args, **kwargs):

        context = {'edupage': ''}
        template = 'education.html'

        return render(request, template, context)