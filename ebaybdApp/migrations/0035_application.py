# Generated by Django 3.1.6 on 2021-03-01 10:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ebaybdApp', '0034_blooddonerregistration'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date created')),
                ('Name', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('phone', models.CharField(max_length=11)),
                ('subject', models.CharField(max_length=100)),
                ('text', models.TextField()),
            ],
        ),
    ]
