# Generated by Django 5.2.1 on 2025-05-12 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_remove_customuser_organization'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='organization',
            name='phone_number',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
