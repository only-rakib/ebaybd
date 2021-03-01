# Generated by Django 3.1.6 on 2021-02-23 15:26

from django.db import migrations, models
import django.utils.timezone
import django_extensions.db.fields
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('ebaybdApp', '0006_covid19_image_for_covid19'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_title', models.CharField(help_text=' প্রকল্পের শিরোনাম দিন ', max_length=100)),
                ('description', tinymce.models.HTMLField(blank=True, help_text=' বর্ন্না লিখুন ')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date created')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='project_title')),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
    ]
