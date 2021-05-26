from django.db import models

THEMES = (
    ('F', 'Funny'),
    ('I', 'Insprational'),
    ('L', 'Love'),
    ('A', 'Advice'),
)

class Quote(models.Model):
    theme = models.CharField(max_length=50)
    author = models.CharField(max_length=100)
    content= models.TextField(max_length=250)
    date = models.DateField()

def __str__(self):
      return f'{self.author} | {self.theme}'



class Category(models.Model):
    category = models.CharField(
        max_length = 1,
        choices=THEMES,
        default=THEMES[0][0]
        #name of the theme and 2nd the actual value
    )
    quote = models.ManyToManyField(Quote, blank=True)
      # Model Methods do not require a migration
def __str__(self):
    return f'{self.category}'
















