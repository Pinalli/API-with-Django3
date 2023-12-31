# Generated by Django 4.2.5 on 2023-10-01 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_registration'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='active',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.EmailField(blank=True, max_length=255, null=True),
        ),
    ]
