# Generated by Django 5.0.4 on 2024-08-05 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qism',
            name='movie',
            field=models.FileField(upload_to='movies/'),
        ),
    ]
