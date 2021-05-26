from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('theme', models.TextField(max_length=50)
                ('content', models.TextField(max_length=100)),
                ('description', models.TextField(max_length=250)),
                ('date',models.DateField())
                )]
        )
    ]
