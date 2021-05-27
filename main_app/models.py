from django.db import models

THEMES = (
    (1,'Funny'),
    (2,'Insprational'),
    (3,'Life'),
    (4,'Advice'),
    (5,'Personal Development'),
    (6,'Rated-RRRRR')
)
class Quote(models.Model):
    theme = models.CharField(max_length=50)
    author = models.CharField(max_length=100)
    content= models.TextField(max_length=250)
    date = models.DateField()


    def __str__(self):
        return f'{self.theme} | {self.author}'

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


# python3 -m venv .env

# source .env/bin/activate

# python3 manage.py runserver

# python3 manage.py makemigrations

# python3 manage.py migrate















