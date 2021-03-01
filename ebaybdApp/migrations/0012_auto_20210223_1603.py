# Generated by Django 3.1.6 on 2021-02-23 16:03

from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('ebaybdApp', '0011_committee_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExecutiveCommittee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.IntegerField(unique=True)),
                ('name', models.CharField(help_text=' নাম  ', max_length=100)),
                ('designation', models.CharField(help_text=' পদবী ', max_length=100)),
                ('occupation', models.CharField(help_text=' পেশা ', max_length=100)),
                ('organization', models.CharField(help_text=' প্রতিষ্ঠান ', max_length=100)),
                ('image', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, help_text='Profile Picture', keep_meta=True, quality=0, size=[1920, 1080], upload_to='images/')),
            ],
            options={
                'ordering': ['serial'],
            },
        ),
        migrations.DeleteModel(
            name='Committee',
        ),
    ]
