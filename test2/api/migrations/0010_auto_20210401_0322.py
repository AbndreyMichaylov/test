# Generated by Django 2.2.10 on 2021-04-01 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20210401_0320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='date_start',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата начала'),
        ),
    ]
