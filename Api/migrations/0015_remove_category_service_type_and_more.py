# Generated by Django 4.1.3 on 2022-12-23 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0014_remove_multiple_category_slider_category_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='service_type',
        ),
        migrations.AddField(
            model_name='multiple_category_slider',
            name='category_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Api.category'),
        ),
        migrations.AlterField(
            model_name='multiple_category_slider',
            name='service_type',
            field=models.CharField(default='', max_length=255),
        ),
    ]
