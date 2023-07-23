# Generated by Django 3.2.13 on 2022-08-01 11:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('presence', '0008_alter_classname_pr'),
    ]

    operations = [
        migrations.AddField(
            model_name='classname',
            name='creator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='class_creator', related_query_name='class_creator', to=settings.AUTH_USER_MODEL),
        ),
    ]
