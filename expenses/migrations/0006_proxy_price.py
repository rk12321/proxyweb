# Generated by Django 4.1.7 on 2023-04-25 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0005_proxy_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='proxy',
            name='price',
            field=models.IntegerField(default=100),
            preserve_default=False,
        ),
    ]