# Generated by Django 4.1.7 on 2023-03-21 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_api', '0004_alter_experience_current_employer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='end_date',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]
