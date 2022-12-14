# Generated by Django 4.1.3 on 2022-12-19 13:18

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0002_delete_saloon_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='saloon_image',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('updated_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('image', models.ImageField(default='', upload_to='superadmin/')),
                ('saloon_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Api.saloon')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
