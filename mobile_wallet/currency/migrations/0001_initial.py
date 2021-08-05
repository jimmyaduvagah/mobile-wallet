# Generated by Django 3.2.5 on 2021-07-06 11:04

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_on', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('created_by', models.UUIDField(blank=True, null=True)),
                ('updated_on', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('updated_by', models.UUIDField(blank=True, null=True)),
                ('country', models.CharField(max_length=100)),
                ('currency_iso_code', models.CharField(max_length=5, unique=True)),
                ('conversion_rate', models.DecimalField(blank=True, decimal_places=4, max_digits=16, null=True)),
            ],
            options={
                'ordering': ('-updated_on', '-created_on'),
                'abstract': False,
            },
        ),
    ]