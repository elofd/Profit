from django.db import models


class MySite(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.IntegerField()

    def __str__(self):
        return self.name
