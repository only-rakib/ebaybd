# Generated by Django 3.1.6 on 2021-02-06 05:21

from django.db import migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('ebaybdApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='project_title'),
        ),
    ]