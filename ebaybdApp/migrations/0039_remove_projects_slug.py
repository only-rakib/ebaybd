# Generated by Django 3.1.6 on 2021-04-10 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ebaybdApp', '0038_auto_20210409_1930'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='slug',
        ),
    ]