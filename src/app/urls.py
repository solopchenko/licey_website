"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from pages.views import PageView
from news.views import NewsView, news_list
from docs.views import DocsView
from staff.views import PersonView
from education.views import ProgramView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    # Админка
    #
    url(r'^admin/', admin.site.urls),

    # Главная страница
    #
    url(r'^$', PageView.as_view(), {'page_url': 'home'}),

    # Докумнты
    #
    url(r'^docs/', DocsView.as_view()),

    # Новости
    #
    url(r'^news/$', news_list),
    url(r'^news/(?P<news_id>[\w-]+)/$', NewsView.as_view()),

    # Сотрудники
    #
    url(r'^staff/(?P<username>[\w-]+)/$', PersonView.as_view()),

    # Программы
    #
    url(r'^education/program/(?P<program_slug>[/\w-]*)/$', ProgramView.as_view()),

    # Страницы
    #
    url(r'^(?P<page_url>[/\w-]*)/$', PageView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)