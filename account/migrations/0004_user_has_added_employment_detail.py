# Generated by Django 3.2.2 on 2021-10-06 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_user_is_unemployed'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='has_added_employment_detail',
            field=models.BooleanField(default=False),
        ),
    ]
