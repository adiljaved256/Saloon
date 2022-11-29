# Generated by Django 4.1.3 on 2022-11-26 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0036_remove_service_register_id_service_added_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='saloon_id',
        ),
        migrations.AddField(
            model_name='employee',
            name='days',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='employee',
            name='endfromtime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='startfromtime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='saloon',
            name='Employee_Detail',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Api.employee'),
        ),
    ]