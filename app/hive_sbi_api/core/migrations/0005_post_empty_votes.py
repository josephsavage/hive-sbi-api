# Generated by Django 4.0.2 on 2022-11-14 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_post_total_rshares'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='empty_votes',
            field=models.BooleanField(default=False),
        ),
    ]