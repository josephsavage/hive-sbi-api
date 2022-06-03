# Generated by Django 4.0.2 on 2022-06-03 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_failedtransaction_remove_transaction_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='failedtransaction',
            name='fail_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Account does not exist'), (2, 'Sponsor does not exist'), (3, 'Empty sponsee'), (4, 'Sponsee acount does not exist'), (5, 'Bad sponsee format')], default=1),
            preserve_default=False,
        ),
    ]
