from django.db import models

# Create your models here.

class Gallery(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')

    def images(self):
        return self.galleryimage_set.all()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галереи'

class GalleryImage(models.Model):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, verbose_name='Галерея')
    file = models.ImageField(verbose_name='Изображение', blank=True)
    href = models.URLField(verbose_name='Ссылка на изображение', blank=True)
    description = models.CharField(max_length=200, verbose_name='Описание изображения', blank=True)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Изображение галереи'
        verbose_name_plural = 'Изображения галерей'