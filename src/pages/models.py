from django.db import models
from staff.models import Person
from docs.models import Document

# Create your models here.

class Page(models.Model):
    HOME_TEMPLATE = 'HOME'
    ABOUT_TEMPLATE = 'ABOUT'
    EDUCATION_TEMPLATE = 'EDUCATION'
    DEFAULT_TEMPLATE = 'PAGE'

    TEMPLATES_CHOICES = (
        (HOME_TEMPLATE, 'Главная страница'),
        (ABOUT_TEMPLATE, 'Страница об организации'),
        (EDUCATION_TEMPLATE, 'Страница образование'),
        (DEFAULT_TEMPLATE, 'Стандартная страница'),
    )

    title = models.CharField(verbose_name='Заголовок', max_length=500)
    parent = models.ForeignKey('self', verbose_name='Родительская страница', on_delete=models.PROTECT, null=True, blank=True)
    slug = models.SlugField(verbose_name='Адрес страницы')
    url = models.CharField(verbose_name='URL', max_length=100)
    template = models.CharField(verbose_name='Шаблон', max_length=500, choices=TEMPLATES_CHOICES, default=DEFAULT_TEMPLATE)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата последнего обновления', auto_now=True)
    author = models.ForeignKey(Person, verbose_name='Автор', on_delete=models.PROTECT)


    def sections(self):
        return self.pagesection_set.all()

    def slider(self):
        return self.pageslide_set.all()

    def parent_pages(self):
        pages = []

        pg = self
        while pg.parent:
            pg = pg.parent
            pages.append(pg)

        return pages

    def children_pages(self):
        return self



    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'
        unique_together = ('parent', 'slug')


class PageSection(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE, verbose_name='Страница')
    title = models.CharField(verbose_name='Заголовок', max_length=200)
    anchor = models.SlugField(verbose_name='Якорная ссылка', blank=True)
    content = models.TextField(verbose_name='Контент', blank=True)
    documents = models.ManyToManyField(Document, verbose_name='Документы', blank=True)
    full_width = models.BooleanField(verbose_name='Секция во всю ширину', help_text='Используется для слайдеров и карт', default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Элемент страницы'
        verbose_name_plural = 'Элементы страницы'


class PageSlide(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE, verbose_name='Страница')
    background_image = models.ImageField(verbose_name='Изображение', upload_to='slider/')
    title = models.CharField(verbose_name='Заголовок', max_length=500)
    subtitle = models.CharField(verbose_name='Подзаголовок', max_length=500, blank=True)
    link = models.URLField(verbose_name='Ссылка на страницу', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Элемент слайдера'
        verbose_name_plural = 'Слайдер'
