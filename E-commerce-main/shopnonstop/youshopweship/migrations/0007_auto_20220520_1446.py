# Generated by Django 3.1 on 2022-05-20 09:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youshopweship', '0006_auto_20220520_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='mobile',
            field=models.CharField(max_length=10, unique=True, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{9,10}$')]),
        ),
    ]
