# Generated by Django 3.1.3 on 2020-11-26 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteapp', '0021_auto_20201127_0408'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='user_name',
            field=models.TextField(max_length=20, null=True),
        ),
    ]
