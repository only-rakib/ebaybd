# Generated by Django 3.1.6 on 2021-04-10 13:24

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('ebaybdApp', '0042_remove_recent_news_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image_for_photo_gallery',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=None, force_format=None, help_text='Picture *Automatic convert into 500*500 pixel', keep_meta=True, quality=-1, size=[1920, 1080], upload_to='albums/'),
        ),
    ]