# Generated by Django 3.2.3 on 2021-05-27 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_quote_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quote',
            name='image',
        ),
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(choices=[('F', 'Funny'), ('I', 'Insprational'), ('L', 'Life'), ('A', 'Advice')], default='F', max_length=1),
        ),
    ]
