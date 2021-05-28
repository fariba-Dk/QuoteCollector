# Generated by Django 3.2.3 on 2021-05-27 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_alter_category_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='quote',
        ),
        migrations.AddField(
            model_name='quote',
            name='category',
            field=models.ManyToManyField(blank=True, to='main_app.Category'),
        ),
    ]