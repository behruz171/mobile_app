# Generated by Django 5.0.4 on 2024-08-05 11:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('question', models.TextField()),
                ('answer', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('release_date', models.DateField()),
                ('duration', models.PositiveIntegerField(blank=True, help_text='Duration in minutes', null=True)),
                ('content_type', models.CharField(choices=[('movie', 'Movie'), ('serial', 'Serial')], max_length=10)),
                ('categories', models.ManyToManyField(to='common.category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('release_date', models.DateField()),
                ('episode_number', models.PositiveIntegerField()),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='episodes', to='common.content')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Qism',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('qism_number', models.PositiveIntegerField()),
                ('movie', models.URLField()),
                ('episode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='qismlar', to='common.episode')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
