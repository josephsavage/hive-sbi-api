# Generated by Django 4.0.2 on 2023-08-07 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_post_has_beneficiaries_post_updated_beneficiaries'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='beneficiaries',
            field=models.JSONField(null=True),
        ),
    ]