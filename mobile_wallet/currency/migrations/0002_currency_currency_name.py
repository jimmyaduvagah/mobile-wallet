# Generated by Django 3.2.5 on 2021-08-07 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='currency',
            name='currency_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]