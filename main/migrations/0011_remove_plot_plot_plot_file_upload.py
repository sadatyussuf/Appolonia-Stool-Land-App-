# Generated by Django 4.0.6 on 2022-07-18 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_plot_options_plot_geom'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plot',
            name='plot',
        ),
        migrations.AddField(
            model_name='plot',
            name='file_upload',
            field=models.FileField(null=True, upload_to='uploads/'),
        ),
    ]