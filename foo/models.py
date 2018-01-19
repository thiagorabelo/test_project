from django.db import models

# Create your models here.

class Foo(models.Model):
    name = models.CharField('Name', max_length=50, blank=False)
    description = models.TextField('Description', null=True)

    def __str__(self):
        return self.name

