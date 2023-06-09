# Generated by Django 4.1.7 on 2023-03-18 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=200)),
                ('school_city', models.CharField(blank=True, max_length=200)),
                ('school_state', models.CharField(blank=True, max_length=200)),
                ('school_country', models.CharField(max_length=200)),
                ('degree_earned', models.CharField(blank=True, max_length=200)),
                ('program', models.CharField(blank=True, max_length=125)),
                ('date_started', models.DateField()),
                ('date_completed', models.DateField()),
                ('accolades', models.CharField(blank=True, max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=200)),
                ('employer_name', models.CharField(max_length=250)),
                ('employer_city', models.CharField(blank=True, max_length=200)),
                ('employer_state', models.CharField(blank=True, max_length=150)),
                ('employer_country', models.CharField(max_length=200)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True)),
                ('current_employer', models.BooleanField(default=False)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Hobby',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('start_date', models.DateField(blank=True)),
                ('end_date', models.DateField(blank=True)),
                ('description', models.TextField(blank=True)),
                ('url', models.URLField(blank=True)),
                ('additional_info', models.CharField(blank=True, max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=125)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('tech_used', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('git_repo', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('level', models.CharField(blank=True, max_length=125)),
                ('type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('url', models.URLField()),
                ('description', models.CharField(blank=True, max_length=175, null=True)),
            ],
        ),
    ]
