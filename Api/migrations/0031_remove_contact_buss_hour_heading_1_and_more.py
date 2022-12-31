# Generated by Django 4.1.3 on 2022-12-30 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0030_contact_buss_hour_discription_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact_buss_hour',
            name='heading_1',
        ),
        migrations.RemoveField(
            model_name='contact_buss_hour',
            name='icon_name',
        ),
        migrations.RemoveField(
            model_name='detail',
            name='saloon_id',
        ),
        migrations.AddField(
            model_name='about_us',
            name='heading_1',
            field=models.CharField(default='', max_length=955),
        ),
        migrations.AddField(
            model_name='contact_buss_hour',
            name='heading_2',
            field=models.CharField(default='', max_length=955),
        ),
        migrations.AddField(
            model_name='pay_cancellation_policy',
            name='heading_6',
            field=models.CharField(default='', max_length=955),
        ),
        migrations.AddField(
            model_name='report',
            name='heading_6',
            field=models.CharField(default='', max_length=955),
        ),
        migrations.AddField(
            model_name='social_media_share',
            name='heading_3',
            field=models.CharField(default='', max_length=955),
        ),
        migrations.AddField(
            model_name='travel_fee_policy',
            name='heading_5',
            field=models.CharField(default='', max_length=955),
        ),
        migrations.AddField(
            model_name='venue_amenitie',
            name='heading_4',
            field=models.CharField(default='', max_length=955),
        ),
    ]
