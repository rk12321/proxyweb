# Generated by Django 4.1.7 on 2023-04-08 20:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0003_proxy_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proxy',
            name='category',
        ),
    ]
