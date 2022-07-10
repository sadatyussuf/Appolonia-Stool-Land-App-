# Generated by Django 3.2.13 on 2022-06-05 02:53

import django.contrib.gis.db.models.fields
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20220429_0150'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('hometown', models.CharField(max_length=54)),
                ('zone', models.CharField(max_length=50)),
                ('phone_number', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 13 digits allowed.", regex='^\\+?1?\\d{9,13}$')])),
                ('plot', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
            ],
        ),
    ]