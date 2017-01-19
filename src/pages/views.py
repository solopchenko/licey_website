from django.shortcuts import render
from django.views import View
from django.shortcuts import get_object_or_404
from app.utils import chunks


from .models import Page
from education.models import EduLevel
from staff.models import Person
from news.models import NewsPage

# Create your views here.
class PageView(View):
    def get(self, request, page_url, *args, **kwargs):

        d = page_url.split('/')
        print(page_url)

        page = get_object_or_404(Page, url=page_url)
        context = {'page': page}

        if page.template == 'HOME':
            news = NewsPage.objects.published().reverse()[:5]
            context['news'] = news

            edu_levels = EduLevel.objects.all()
            context['edu_levels'] = edu_levels

            person_chunks = chunks(Person.objects.staff(), 3)
            context['person_chunks'] = person_chunks

            template = 'home.html'

        elif page.template == 'EDUCATION':
            edu_levels = EduLevel.objects.all()
            context['edu_levels'] = edu_levels

            template = 'education.html'

        elif page.template == 'ABOUT':
            template = 'about.html'

        else:
            template = 'page.html'

        return render(request, template, context)