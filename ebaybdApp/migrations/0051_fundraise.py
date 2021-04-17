# Generated by Django 3.1.6 on 2021-04-14 16:45

from django.db import migrations, models
import django.utils.timezone
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('ebaybdApp', '0050_auto_20210412_0012'),
    ]

    operations = [
        migrations.CreateModel(
            name='FundRaise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date created')),
                ('title', models.CharField(max_length=200)),
                ('quote', models.CharField(blank=True, max_length=200)),
                ('description', tinymce.models.HTMLField(blank=True, help_text=' Description ')),
                ('targeted_amount', models.CharField(max_length=10)),
                ('raised_amount', models.CharField(max_length=10)),
                ('image', models.ImageField(upload_to='images')),
                ('active', models.BooleanField()),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
    ]