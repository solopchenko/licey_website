from django.db import models

# Create your models here.
class DocumentCategoryManager(models.Manager):
    def published(self, *args, **kwargs):
        qs = super(DocumentCategoryManager, self).all(*args, **kwargs)
        return qs.filter(published=True)

class DocumentCategory(models.Model):
    name = models.CharField(verbose_name='Наименование', max_length=200)
    published = models.BooleanField(verbose_name='Отображать на странице документов', default=False)
    description = models.TextField(verbose_name='Описание', blank=True)

    objects = DocumentCategoryManager()

    def documents(self):
        return self.document_set.all()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория документа'
        verbose_name_plural = 'Категория документов'

class DocumentSubcategory(models.Model):
    pass


class Document(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=500)
    category = models.ForeignKey(DocumentCategory, on_delete=models.PROTECT)
    link = models.URLField(verbose_name='Ссылка на документ', blank=True)
    file = models.FileField(verbose_name='Файл', upload_to='docs/', blank=True)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата обновления', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'