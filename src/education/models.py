from django.db import models
from docs.models import DocumentCategory, Document

# Create your models here.

class EduLevel(models.Model):
    name = models.CharField(verbose_name='Наименование', max_length=200)
    description = models.TextField(verbose_name='Описание')

    def programs(self):
        return self.eduprogram_set.all()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Ступень образования"
        verbose_name_plural = "Ступени образования"

class EduCourse(models.Model):
    name = models.CharField(verbose_name='Наименование', max_length=200)
    description = models.CharField(verbose_name='Описание', max_length=200, blank=True, help_text='Вспомогательная информация, которая не видна посетителям сайта.')
    course_program =  models.ForeignKey(Document, verbose_name='Рабочая программа дисциплины', on_delete=models.PROTECT, blank=True, null=True)
    annotations = models.ManyToManyField(Document, verbose_name='Аннотации рабочей программы дисциплины', blank=True, related_name='course_annotations')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Дисциплина"
        verbose_name_plural = "Дисциплины"

class EduProgram(models.Model):
    name = models.CharField(verbose_name='Наименование', max_length=200)
    slug = models.SlugField(verbose_name='Страница образовательной программы', unique=True)
    form = models.ForeignKey(EduLevel, verbose_name='Ступень образования', on_delete=models.PROTECT)
    description = models.CharField(verbose_name='Краткое описание', max_length=200, help_text='Например, автор программы.')
    full_description = models.TextField(verbose_name='Подробное описание', blank=True, max_length=500, help_text='Отображается на странице образовательной программы.')
    courses = models.ManyToManyField(EduCourse, verbose_name='Дисциплины', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Образовательная программа"
        verbose_name_plural = "Образовательные программы"

# class EduPage(models.Model):
#     title = models.CharField(verbose_name='Заголовок', max_length=500)
#     show_programs = models.BooleanField(verbose_name='Показывать список образовательных программ', blank=False, default=True)
#
# class EduPageSection(models.Model):
#     title = models.CharField(verbose_name='Заголовок', max_length=500)
#     content = models.TextField(verbose_name='Контент', blank=True)
#     documents = models.ManyToManyField(Document, verbose_name='Документы', blank=True)
