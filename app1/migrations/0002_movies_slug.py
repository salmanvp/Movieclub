# Generated by Django 4.2.3 on 2023-08-10 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='slug',
            field=models.SlugField(max_length=10, null=True, unique=True),
        ),
    ]
