# Generated by Django 3.1.6 on 2021-02-06 14:24

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('ebaybdApp', '0002_auto_20210206_0521'),
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media_title', models.CharField(max_length=120)),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='title')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date created')),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
        migrations.CreateModel(
            name='Press',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='title')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date created')),
                ('media', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='title', to='ebaybdApp.media')),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
    ]