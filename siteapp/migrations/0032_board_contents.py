# Generated by Django 3.1.3 on 2020-11-27 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteapp', '0031_remove_content_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='contents',
            field=models.ManyToManyField(blank=True, related_name='contents', to='siteapp.Content'),
        ),
    ]
