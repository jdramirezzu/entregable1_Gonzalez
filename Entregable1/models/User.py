from django.db import models


# Create your models here.
class User(models.Model):
    userId = models.IntegerField()

    def __init__(self, userId, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.userId = userId
