# Generated by Django 4.2.11 on 2024-04-24 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vortex_app', '0005_imagedownload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagedownload',
            name='date',
            field=models.DateField(),
        ),
    ]