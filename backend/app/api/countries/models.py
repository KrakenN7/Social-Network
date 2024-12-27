from django.db import models


class Countries(models.Model):
    name = models.CharField(max_length=30)
    alpha2 = models.CharField(max_length=2)
    alpha3 = models.CharField(max_length=3)
    region = models.CharField(max_length=30)

    class Meta:
        db_table = "countries"

    def __str__(self):
        return self.name
