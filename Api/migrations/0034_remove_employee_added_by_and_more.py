# Generated by Django 4.1.3 on 2022-12-30 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0033_rename_heading_1_about_us_heading_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='Added_by',
        ),
        migrations.AlterField(
            model_name='health_safety_rule',
            name='name',
            field=models.CharField(default='', max_length=555),
        ),
    ]