# Generated by Django 4.0.2 on 2022-11-10 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_post_vote'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='total_rshares',
            field=models.BigIntegerField(default=0),
            preserve_default=False,
        ),
    ]