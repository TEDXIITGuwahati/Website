# Generated by Django 3.0.1 on 2020-01-11 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20191115_2307'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='link',
            field=models.TextField(default='https://medium.com/'),
        ),
    ]