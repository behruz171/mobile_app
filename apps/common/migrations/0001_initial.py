# Generated by Django 5.0.3 on 2024-03-18 14:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('full_name', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=20)),
                ('wallet', models.DecimalField(decimal_places=2, max_digits=12)),
                ('status', models.CharField(choices=[('new', 'New'), ('moderation', 'Moderation'), ('approved', 'Approved'), ('canceled', 'Canceled')], default='new', max_length=20)),
                ('payment_type', models.CharField(choices=[('cash', 'Cash'), ('by_card', 'By card')], max_length=20, null=True)),
                ('company_name', models.CharField(max_length=200, null=True)),
                ('user_type', models.CharField(choices=[('physical', 'Physical'), ('legal', 'Legal')], default='physical', max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('full_name', models.CharField(max_length=200)),
                ('degree', models.CharField(choices=[('bachelor', 'Bachelor'), ('master', 'Master')], default='bachelor', max_length=20)),
                ('contract', models.DecimalField(decimal_places=2, max_digits=12)),
                ('phone_number', models.CharField(max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StudentSponser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('sponsor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_amounts', to='common.sponsor')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sponsor_amounts', to='common.student')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='student',
            name='university',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='students', to='common.university'),
        ),
    ]
