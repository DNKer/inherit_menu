# Generated by Django 3.2 on 2023-04-28 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0006_auto_20230428_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='url',
            field=models.CharField(default='default `Item name`', max_length=255, verbose_name='URL подменю'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='url',
            field=models.CharField(default='default `Menu name`', max_length=255, verbose_name='URL меню'),
        ),
    ]