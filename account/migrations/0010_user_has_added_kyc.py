# Generated by Django 3.2.2 on 2021-10-20 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_auto_20211020_1603'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='has_added_kyc',
            field=models.BooleanField(default=False),
        ),
    ]
