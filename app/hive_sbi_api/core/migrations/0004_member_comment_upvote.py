# Generated by Django 4.0.2 on 2022-04-05 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_member_estimate_rewarded'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='comment_upvote',
            field=models.BooleanField(default=False),
        ),
    ]