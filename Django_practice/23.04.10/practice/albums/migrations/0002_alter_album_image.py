# Generated by Django 3.2.18 on 2023-04-10 07:56

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(blank=True, upload_to='%Y/%m/%d'),
        ),
    ]
