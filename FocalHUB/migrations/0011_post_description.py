# Generated by Django 4.2.1 on 2023-06-05 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FocalHUB', '0010_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
