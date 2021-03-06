# Generated by Django 3.2.2 on 2021-12-27 19:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_userprofile_volunter_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='highschool',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2021, 12, 27, 19, 38, 8, 374483, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='highschool',
            name='expected_end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='socialmedia',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2021, 12, 27, 19, 38, 13, 371859, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tertiaryinstitution',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2021, 12, 27, 19, 38, 18, 193906, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trainingpathway',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2021, 12, 27, 19, 38, 21, 315629, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='useremploymentdetail',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2021, 12, 27, 19, 38, 23, 668822, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='useridentity',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2021, 12, 27, 19, 38, 25, 586904, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2021, 12, 27, 19, 38, 27, 526643, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='highschool',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tertiaryinstitution',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
