from django.db import models

class NewsPageManager(models.Manager):
    def published(self, *args, **kwargs):
        qs = super(NewsPageManager, self).all(*args, **kwargs)
        return qs.filter(published=True)
