# Generated by Django 3.2.5 on 2021-08-08 15:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_category_herbicide_insecticide_pesticide'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
    ]
