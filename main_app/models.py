from django.db import models


class Quote(models.Model):
    theme= models.CharField(max_length=100)
    content= models.TextField()
    date_added = models.DateField()
    # author= models.ForeignKey



