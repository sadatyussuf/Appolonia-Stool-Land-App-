# Generated by Django 4.0.6 on 2022-08-07 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_plot_geom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plot',
            name='address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='plot',
            name='hometown',
            field=models.CharField(blank=True, max_length=54, null=True),
        ),
        migrations.AlterField(
            model_name='plot',
            name='owner_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='plot',
            name='zone',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]