from django.shortcuts import render
from django.views import View
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import NewsPage

# Create your views here.
class NewsView(View):
    def get(self, request, news_id):
        news = get_object_or_404(NewsPage, id=news_id, published=True)
        return render(request, 'news/news.html', {'news': news})

def news_list(request):
    news_objects = NewsPage.objects.published()
    paginator = Paginator(news_objects, 10)

    page = request.GET.get('page')
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)

    return render(request, 'news/list.html', {'news': news})