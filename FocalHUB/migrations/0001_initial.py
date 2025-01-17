# Generated by Django 4.2.1 on 2023-05-28 21:18

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('upload_date', models.DateField(auto_now_add=True)),
                ('likes', models.ManyToManyField(related_name='picture_likes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
