# Generated by Django 3.1.6 on 2021-02-22 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ebaybdApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='default',
        ),
    ]