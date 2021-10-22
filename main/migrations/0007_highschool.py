# Generated by Django 3.2.2 on 2021-10-11 15:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0006_auto_20211011_1405'),
    ]

    operations = [
        migrations.CreateModel(
            name='HighSchool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=300)),
                ('institution', models.CharField(max_length=3600)),
                ('qualification', models.CharField(max_length=300)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(null=True)),
                ('complete', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='high_schools', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
