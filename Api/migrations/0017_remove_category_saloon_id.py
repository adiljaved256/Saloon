# Generated by Django 4.1.3 on 2022-12-26 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0016_category_saloon_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='saloon_id',
        ),
    ]
