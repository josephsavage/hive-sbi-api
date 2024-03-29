# Generated by Django 4.0.2 on 2022-11-08 02:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20220912_1538'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=50)),
                ('permlink', models.CharField(max_length=512)),
                ('title', models.TextField()),
                ('created', models.DateTimeField()),
                ('vote_rshares', models.BigIntegerField()),
                ('total_payout_value', models.FloatField()),
                ('author_rewards', models.FloatField()),
                ('active_votes', models.JSONField(null=True)),
            ],
            options={
                'verbose_name': 'post',
                'verbose_name_plural': 'posts',
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voter', models.CharField(max_length=50)),
                ('weight', models.BigIntegerField()),
                ('rshares', models.BigIntegerField()),
                ('percent', models.BigIntegerField()),
                ('reputation', models.BigIntegerField()),
                ('time', models.DateTimeField()),
                ('member_hist_datetime', models.DateTimeField()),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.post', verbose_name='post')),
            ],
            options={
                'verbose_name': 'vote',
                'verbose_name_plural': 'votes',
                'ordering': ['time'],
            },
        ),
    ]
