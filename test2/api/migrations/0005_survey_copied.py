# Generated by Django 2.2.10 on 2021-03-31 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_delete_startedsurvey'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='copied',
            field=models.BooleanField(default=False, verbose_name='Копировано'),
        ),
    ]
