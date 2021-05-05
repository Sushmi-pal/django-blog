# Generated by Django 3.1.2 on 2021-04-29 09:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('landing', '0002_auto_20210429_0649'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogview',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]