# Generated by Django 4.1.2 on 2022-10-10 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_remove_workexperience_cover_aboutus_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='myproject',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]