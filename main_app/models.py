from django.db import models

THEMES = (
    ('F','Funny'),
    ('I','Insprational'),
    ('L','Life'),
    ('A','Advice'),
    ('P','Personal Development'),
    ('R','Rated-RRRRR')
)

class Category(models.Model):
    category = models.CharField(
        max_length = 1,
        choices=THEMES,
        default=THEMES[0][0]

        #name of the theme and 2nd the actual value
    )
    def __str__(self):
        return f'{self.get_category_display()}'


class Quote(models.Model):
    theme = models.CharField(max_length=50)
    author = models.CharField(max_length=100)
    content= models.TextField(max_length=250)
    date = models.DateField()

    category = models.ManyToManyField(Category, blank=True)

    def __str__(self):
        return f'{self.theme}'



# python3 -m venv .env


# source .env/bin/activate

# python3 manage.py runserver

# python3 manage.py makemigrations

# python3 manage.py migrate















