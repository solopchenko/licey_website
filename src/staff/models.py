from django.db import models
from django.contrib.auth.models import User
from .managers import PersonManager

# Create your models here.
class PersonPosition(models.Model):
    name = models.CharField(max_length=200, verbose_name='Наименование должности')
    administration = models.BooleanField(default=False, verbose_name='Администрация')

    def persons(self):
        return self.person_set.all()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'

class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Логин (пользователь)')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    middle_name = models.CharField(max_length=50, verbose_name='Отчество', blank=True)
    photo = models.ImageField(verbose_name='Фотография', blank=True)
    email = models.EmailField(verbose_name='Электронная почта', blank=True)
    phone = models.CharField(max_length=20, verbose_name='Телефон', blank=True)
    office = models.CharField(max_length=100, verbose_name='Кабинет')
    education = models.CharField(max_length=500, verbose_name='Образование', blank=True)
    teaching_experience = models.CharField(max_length=200, verbose_name='Педагогический стаж', blank=True)
    positions = models.ManyToManyField(PersonPosition, verbose_name='Должности', blank=True)


    objects = PersonManager()

    def tabs(self):
        return self.persontab_set.all()

    def full_name(self):
        if self.middle_name:
            return self.last_name + ' ' + self.first_name + ' ' + self.middle_name
        else:
            return self.last_name + ' ' + self.first_name

    def all_positions(self):
        pos = self.positions.all()
        s = pos[0]
        for i in range(1, len(pos)):
            s = s + ', ' + self.positions[i].name
        return s

    def __str__(self):
        return self.full_name()

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
        ordering = ['last_name', 'first_name', 'middle_name']


class PersonTab(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название вкладки')
    content = models.TextField(verbose_name='Контент вкладки')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлена')
    person = models.ForeignKey(Person, on_delete=models.CASCADE, verbose_name='Сотрудник')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вкладка'
        verbose_name_plural = 'Вкладки'