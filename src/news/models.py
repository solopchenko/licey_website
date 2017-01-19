from django.db import models

from .validators import no_future_date
from .managers import NewsPageManager

from app.utils import get_now
from staff.models import Person
from gallery.models import Gallery

# Create your models here.
class NewsPage(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=500)
    announcement = models.TextField(verbose_name='Анонс', max_length=200, help_text='Отображается вверху новости. Форматирование текста <b>не поддерживается.</b>')
    content = models.TextField(verbose_name='Контент')
    #gallery = models.ForeignKey(Gallery, blank=True, null=True, verbose_name='Галерея')
    author = models.ForeignKey(Person, on_delete=models.PROTECT, verbose_name='Автор')
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата обновления', auto_now=True)
    published_at = models.DateTimeField(verbose_name='Дата публикации', null=True, blank=True, validators=[no_future_date])
    published = models.BooleanField(verbose_name='Опубликовать')

    objects = NewsPageManager()

    def gallery(self):
        return self.newspagegalleryimage_set.all()

    def save(self, *args, **kwargs):

        if self.published:
            if self.published_at is None:
                self.published_at = get_now()
        else:
            self.published_at = None

        super(NewsPage, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-published_at']

class NewsPageGalleryImage(models.Model):
    news_page = models.ForeignKey(NewsPage, on_delete=models.CASCADE, verbose_name='Новость')
    file = models.ImageField(verbose_name='Изображение', blank=True)
    href = models.URLField(verbose_name='Ссылка на изображение', blank=True)
    description = models.CharField(max_length=200, verbose_name='Описание изображения', blank=True)

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = 'Изображение галереи'
        verbose_name_plural = 'Галерея'