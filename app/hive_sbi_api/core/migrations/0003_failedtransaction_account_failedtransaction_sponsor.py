# Generated by Django 4.0.2 on 2022-09-11 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20220911_1658'),
    ]

    operations = [
        migrations.AddField(
            model_name='failedtransaction',
            name='account',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='failedtransaction',
            name='sponsor',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]