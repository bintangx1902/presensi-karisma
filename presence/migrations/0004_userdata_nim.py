# Generated by Django 3.2.13 on 2022-07-27 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('presence', '0003_recap'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='nim',
            field=models.CharField(default=0, max_length=255),
        ),
    ]
