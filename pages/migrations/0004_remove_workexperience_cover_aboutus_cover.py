# Generated by Django 4.1.2 on 2022-10-10 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_myproject_workexperience_cover'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workexperience',
            name='cover',
        ),
        migrations.AddField(
            model_name='aboutus',
            name='cover',
            field=models.ImageField(blank=True, upload_to='my_picture/'),
        ),
    ]