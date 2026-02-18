# app/hive_sbi_api/core/migrations/00xx_postvotes_table.py
from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ("core", "0010_post_curator_payout_value_post_percent_hbd"),
    ]

    operations = [
        migrations.CreateModel(
            name="PostVotes",
            fields=[
                ("post", models.OneToOneField(
                    on_delete=django.db.models.deletion.CASCADE,
                    primary_key=True,
                    serialize=False,
                    related_name="votes_payload",
                    to="core.post",
                )),
                ("active_votes", models.JSONField(null=True, blank=True)),
                ("beneficiaries", models.JSONField(null=True, blank=True)),
            ],
            options={
                "db_table": "core_post_votes",
            },
        ),
    ]
