# Generated by Django 4.1.6 on 2023-02-24 16:27

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='user',
        ),
        migrations.AddField(
            model_name='customer',
            name='users',
            field=models.ManyToManyField(null=True, related_name='users', to=settings.AUTH_USER_MODEL),
        ),
    ]