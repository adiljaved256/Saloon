# Generated by Django 4.1.3 on 2022-12-08 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0051_remove_saloon_role_id_remove_service_added_by_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='description',
            new_name='name',
        ),
    ]