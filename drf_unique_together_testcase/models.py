from django.conf import settings
from django.db import models


class Thing(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    name = models.CharField(max_length=64)

    class Meta:
        unique_together = (('owner', 'name'),)
