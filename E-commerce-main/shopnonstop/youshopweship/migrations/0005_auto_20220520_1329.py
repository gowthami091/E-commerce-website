# Generated by Django 3.1 on 2022-05-20 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youshopweship', '0004_auto_20210421_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
