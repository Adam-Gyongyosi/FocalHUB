# Generated by Django 4.2.1 on 2023-06-03 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FocalHUB', '0007_remove_post_likes_post_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
