# Generated by Django 4.1.3 on 2022-12-06 14:07

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0048_role_employee_added_by_register_role_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('updated_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('firstname', models.CharField(default='', max_length=255)),
                ('lastname', models.CharField(default='', max_length=255)),
                ('email', models.EmailField(default='', max_length=255)),
                ('password', models.CharField(default='', max_length=255)),
                ('contact', models.CharField(default='', max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='country',
            name='account_id',
        ),
        migrations.AddField(
            model_name='country',
            name='Account_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Api.account'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='register_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Api.account'),
        ),
        migrations.AlterField(
            model_name='category',
            name='role_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Api.account'),
        ),
        migrations.AlterField(
            model_name='package',
            name='register_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Api.account'),
        ),
        migrations.AlterField(
            model_name='whitelisttoken',
            name='role_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Api.account'),
        ),
        migrations.DeleteModel(
            name='register',
        ),
    ]
