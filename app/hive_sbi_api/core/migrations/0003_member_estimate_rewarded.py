# Generated by Django 4.0.2 on 2022-03-28 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20220323_2143'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='estimate_rewarded',
            field=models.FloatField(default=0),
        ),
    ]