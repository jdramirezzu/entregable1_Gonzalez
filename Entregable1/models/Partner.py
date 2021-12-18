from django.db import models


# Create your models here.
class Partner(models.Model):
    name = models.CharField(max_length=40)

    def __init__(self, name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name

