from django.db import models
from docs.models import Document
from staff.models import Person
from django.contrib.auth.models import User

# Create your models here.
class Organisation(models.Model):
    full_name = models.CharField(verbose_name='Полное наименование', max_length=500)
    short_name = models.CharField(verbose_name='Сокращенное наименование', max_length=200, blank=True)
    foundation_date = models.DateField(verbose_name='Дата ввода в эксплуатацию')
    registration_date = models.DateField(verbose_name='Дата государственной регистрации')
    accreditation = models.ForeignKey(Document, on_delete=models.PROTECT, verbose_name='Акредитация', blank=True, null=True)
    director = models.ForeignKey(Person, on_delete=models.PROTECT, verbose_name='Директор', blank=True, null=True)

    email = models.EmailField(verbose_name='Адрес электронной почты')
    website = models.URLField(verbose_name='Сайт')

    def name(self):
        if self.short_name:
            return self.short_name
        else:
            return self.full_name

    def founders(self):
        return self.organisationfounder_set.all()

    def buildings(self):
        return self.organisationbuilding_set.all()

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Информация об организации'
        verbose_name_plural = 'Информация об организации'

class OrganisationBuilding(models.Model):
    name = models.CharField(verbose_name='Наименование здания', max_length=500)
    address = models.CharField(verbose_name='Адрес', max_length=500)
    phone = models.CharField(verbose_name='Телефон', max_length=25, blank=True)
    business_hours = models.TextField(verbose_name='Часы работы', max_length=500)
    visiting_hours = models.TextField(verbose_name='Часы приема', max_length=500, blank=True)
    organisation = models.ForeignKey(Organisation, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Филиал'
        verbose_name_plural = 'Филиалы'


class OrganisationFounder(models.Model):
    name = models.CharField(verbose_name='Наименование организации', max_length=500)
    head = models.CharField(verbose_name='Руководитель', max_length=500)
    address = models.CharField(verbose_name='Адрес', max_length=500)
    phone = models.CharField(verbose_name='Телефон', max_length=25)
    website = models.URLField(verbose_name='Сайт', blank=True)
    email = models.EmailField(verbose_name='Адрес электронной почты', blank=True)
    feedback = models.URLField(verbose_name='Электронная приёмная', blank=True)
    business_hours = models.TextField(verbose_name='Часы работы', max_length=500)
    visiting_hours = models.TextField(verbose_name='Часы приема', max_length=500, blank=True)
    organisation = models.ForeignKey(Organisation, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Учредитель'
        verbose_name_plural = "Учредители"


MAIN_NAVIGATION = 'MAIN'
FOOTER_NAVIGATION = 'FOOTER'

NAVIGATION_CHOICES = (
    (MAIN_NAVIGATION, 'Верхнее меню главной страницы'),
    (FOOTER_NAVIGATION, 'Нижнее меню '),
)


class MenuManager(models.Manager):
    def footer(self, *args, **kwargs):
        qs = super(MenuManager, self).all(*args, **kwargs)
        return qs.filter(position=FOOTER_NAVIGATION)

    def main(self, *args, **kwargs):
        qs = super(MenuManager, self).all(*args, **kwargs)
        return qs.filter(position=MAIN_NAVIGATION)


class Menu(models.Model):
    name = models.CharField(verbose_name='Наименование меню', max_length=500)
    href = models.CharField(verbose_name='Ссылка', max_length=200, blank=True)
    position = models.CharField(verbose_name='Расположение', max_length=500, choices=NAVIGATION_CHOICES, default=MAIN_NAVIGATION)
    objects = MenuManager()

    def links(self):
        return self.menulink_set.all()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'


class MenuLink(models.Model):
    title = models.CharField(verbose_name='Наименование', max_length=500)
    href = models.CharField(verbose_name='Ссылка', max_length=200)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, verbose_name='Меню')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Ссылка в меню'
        verbose_name_plural = 'Ссылки в меню'