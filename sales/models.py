from django.db import models


class Sale(models.Model):
    PLZ = models.TextField()
    Summe = models.TextField()




