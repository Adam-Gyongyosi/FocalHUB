# Generated by Django 4.2.1 on 2023-05-29 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FocalHUB', '0004_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='media/images'),
        ),
    ]