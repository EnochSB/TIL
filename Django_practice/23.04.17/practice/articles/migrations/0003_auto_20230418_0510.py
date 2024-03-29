# Generated by Django 3.2.18 on 2023-04-17 20:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0002_auto_20230418_0143'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='like_users',
        ),
        migrations.CreateModel(
            name='Emote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emotion', models.CharField(max_length=10)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.article')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='emote_users',
            field=models.ManyToManyField(related_name='emote_users', through='articles.Emote', to=settings.AUTH_USER_MODEL),
        ),
    ]
