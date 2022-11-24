# Generated by Django 4.1.3 on 2022-11-23 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0028_rename_role_name_register_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='saloon',
            name='role_id',
        ),
        migrations.AddField(
            model_name='saloon',
            name='role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Api.role'),
        ),
    ]