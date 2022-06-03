# Generated by Django 4.0.2 on 2022-06-03 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Configuration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('share_cycle_min', models.FloatField(default=144)),
                ('sp_share_ratio', models.FloatField(default=2)),
                ('rshares_per_cycle', models.BigIntegerField(default=800000000, null=True)),
                ('del_rshares_per_cycle', models.BigIntegerField(default=800000000)),
                ('comment_vote_divider', models.FloatField(null=True)),
                ('comment_vote_timeout_h', models.FloatField(null=True)),
                ('last_cycle', models.DateTimeField(null=True)),
                ('upvote_multiplier', models.FloatField(default=1.05)),
                ('upvote_multiplier_adjusted', models.FloatField(default=1)),
                ('last_paid_post', models.DateTimeField(null=True)),
                ('last_paid_comment', models.DateTimeField()),
                ('minimum_vote_threshold', models.BigIntegerField(default=800000000)),
                ('last_delegation_check', models.DateTimeField(null=True)),
                ('comment_footer', models.TextField(null=True)),
            ],
            options={
                'verbose_name': 'configuration',
                'verbose_name_plural': 'configuration',
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.CharField(max_length=50, unique=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('shares', models.PositiveIntegerField()),
                ('bonus_shares', models.PositiveIntegerField()),
                ('total_shares', models.PositiveBigIntegerField(default=0)),
                ('total_share_days', models.PositiveIntegerField(null=True)),
                ('avg_share_age', models.FloatField(null=True)),
                ('last_comment', models.DateTimeField(null=True)),
                ('last_post', models.DateTimeField(null=True)),
                ('original_enrollment', models.DateTimeField(null=True)),
                ('latest_enrollment', models.DateTimeField(null=True)),
                ('flags', models.TextField(blank=True, null=True)),
                ('earned_rshares', models.PositiveBigIntegerField(null=True)),
                ('subscribed_rshares', models.PositiveBigIntegerField(default=0)),
                ('curation_rshares', models.PositiveBigIntegerField(default=0)),
                ('delegation_rshares', models.PositiveBigIntegerField(default=0)),
                ('other_rshares', models.PositiveBigIntegerField(default=0)),
                ('rewarded_rshares', models.PositiveBigIntegerField(null=True)),
                ('pending_balance', models.FloatField(default=0)),
                ('estimate_rewarded', models.FloatField(default=0)),
                ('next_upvote_estimate', models.FloatField(default=0)),
                ('balance_rshares', models.BigIntegerField(null=True)),
                ('total_rshares', models.BigIntegerField(null=True)),
                ('upvote_delay', models.FloatField(null=True)),
                ('updated_at', models.DateTimeField()),
                ('first_cycle_at', models.DateTimeField()),
                ('last_received_vote', models.DateTimeField(null=True)),
                ('blacklisted', models.BooleanField(null=True)),
                ('hivewatchers', models.BooleanField()),
                ('buildawhale', models.BooleanField()),
                ('comment_upvote', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'member',
                'verbose_name_plural': 'members',
                'ordering': ['-total_shares'],
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('index', models.BigIntegerField(primary_key=True, serialize=False)),
                ('source', models.CharField(choices=[('mgmt', 'mgmt'), ('steembasicincome', 'steembasicincome'), ('sbi10', 'sbi10'), ('sbi9', 'sbi9'), ('sbi8', 'sbi8'), ('sbi7', 'sbi7'), ('sbi6', 'sbi6'), ('sbi5', 'sbi5'), ('sbi4', 'sbi4'), ('sbi3', 'sbi3'), ('sbi2', 'sbi2'), ('shares', 'shares')], max_length=50)),
                ('memo', models.TextField(blank=True, null=True)),
                ('shares', models.IntegerField(null=True)),
                ('vests', models.FloatField(null=True)),
                ('timestamp', models.DateTimeField()),
                ('status', models.CharField(choices=[('Valid', 'Valid'), ('Refunded', 'Refunded'), ('AccountDoesNotExist', 'AccountDoesNotExist'), ('Refused', 'Refused'), ('LessOrNoSponsee', 'LessOrNoSponsee')], max_length=50)),
                ('share_type', models.CharField(choices=[('Mgmt', 'Mgmt'), ('Standard', 'Standard'), ('Delegation', 'Delegation'), ('SBD', 'SBD'), ('Refund', 'Refund'), ('RemovedDelegation', 'RemovedDelegation'), ('DelegationLeased', 'DelegationLeased'), ('Refunded', 'Refunded'), ('MgmtTransfer', 'MgmtTransfer'), ('ShareTransfer', 'ShareTransfer'), ('HBD', 'HBD')], max_length=50)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.member', verbose_name='account')),
                ('sponsor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sponsor', to='core.member', verbose_name='sponsor')),
            ],
            options={
                'verbose_name': 'transaction',
                'verbose_name_plural': 'transactions',
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='Sponsee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('units', models.IntegerField()),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.member', verbose_name='account')),
                ('trx', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sponsees', to='core.transaction', verbose_name='trx')),
            ],
            options={
                'verbose_name': 'sponsee',
                'verbose_name_plural': 'sponsees',
                'ordering': ['account'],
            },
        ),
        migrations.CreateModel(
            name='FailedTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trx_index', models.BigIntegerField()),
                ('fail_type', models.PositiveSmallIntegerField(choices=[(1, 'Account does not exist'), (2, 'Sponsor does not exist'), (3, 'Empty sponsee'), (4, 'Sponsee acount does not exist'), (5, 'Bad sponsee format'), (6, 'index already exists')])),
                ('description', models.TextField(blank=True, null=True)),
                ('spoonse_text', models.TextField(blank=True, null=True)),
                ('is_solved', models.BooleanField(default=False)),
                ('transaction', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.transaction', verbose_name='transaction')),
            ],
            options={
                'verbose_name': 'failed transaction',
                'verbose_name_plural': 'failed transactions',
                'ordering': ['-transaction'],
            },
        ),
    ]
