# Generated by Django 4.1.3 on 2022-12-29 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0028_remove_about_us_contact_buss_hour_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='saloon_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Api.saloon'),
        ),
    ]
