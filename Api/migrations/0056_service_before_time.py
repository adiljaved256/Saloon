# Generated by Django 4.1.3 on 2022-12-10 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0055_service_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='before_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
