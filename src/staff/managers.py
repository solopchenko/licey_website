from django.db import models

class PersonManager(models.Manager):
    def staff(self, *args, **kwargs):
        qs = super(PersonManager, self).all(*args, **kwargs)
        return qs.filter(positions__isnull=False).distinct()