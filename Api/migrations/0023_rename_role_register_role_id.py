# Generated by Django 4.1.3 on 2022-11-22 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0022_rename_role_id_register_role'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register',
            old_name='role',
            new_name='role_id',
        ),
    ]
