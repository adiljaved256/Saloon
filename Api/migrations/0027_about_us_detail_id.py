# Generated by Django 4.1.3 on 2022-12-29 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0026_detail_venue_amenitie_travel_fee_policy_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='about_us',
            name='detail_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Api.detail'),
        ),
    ]
