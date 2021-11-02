from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class model(models.Model):
    base = models.CharField('TODO', max_length=300, blank=False)

    def __str__(self):
        return self.base