from django.db import models


class SBIManager(models.Manager):
    def __init__(self):
        super().__init__()
        self._db = 'sbi'


class SBIMember(models.Model):
    objects = SBIManager()

    account = models.CharField(
        primary_key=True,
        max_length=50,
    )

    note = models.TextField(
        null=True,
    )

    shares = models.IntegerField()

    bonus_shares = models.IntegerField()

    total_share_days = models.IntegerField(
        null=True,
    )

    avg_share_age = models.FloatField(
        null=True,
    )

    last_comment = models.DateTimeField(
        null=True,
    )

    last_post = models.DateTimeField(
        null=True,
    )

    original_enrollment = models.DateTimeField(
        null=True,
    )

    latest_enrollment = models.DateTimeField(
        null=True,
    )

    flags = models.TextField(
        null=True,
    )

    earned_rshares = models.BigIntegerField(
        null=True,
    )

    subscribed_rshares = models.BigIntegerField(
        default=0,
    )

    curation_rshares = models.BigIntegerField(
        default=0,
    )

    delegation_rshares = models.BigIntegerField(
        default=0,
    )

    other_rshares = models.BigIntegerField(
        default=0,
    )

    rewarded_rshares = models.BigIntegerField(
        null=True,
    )

    balance_rshares =  models.BigIntegerField(
        null=True,
    )

    upvote_delay = models.FloatField(
        null=True,
    )

    updated_at = models.DateTimeField()
    first_cycle_at = models.DateTimeField()

    last_received_vote = models.DateTimeField(
        null=True,
    )

    blacklisted = models.BooleanField(
        null=True,
    )

    hivewatchers = models.BooleanField(
        null=True,
    )
    buildawhale = models.BooleanField(
        null=True,
    )

    def __str__(self):
        return self.account

    class Meta:
        managed = False
        db_table = 'member'



class SBIConfiguration(models.Model):
    objects = SBIManager()

    share_cycle_min = models.FloatField()

    sp_share_ratio = models.FloatField()

    rshares_per_cycle = models.BigIntegerField(
        null=True,
    )

    del_rshares_per_cycle = models.BigIntegerField()

    comment_vote_divider = models.FloatField(
        null=True,
    )

    comment_vote_timeout_h = models.FloatField(
        null=True,
    )

    last_cycle = models.DateTimeField(
        null=True,
    )

    upvote_multiplier = models.FloatField()

    upvote_multiplier_adjusted = models.FloatField()

    last_paid_post = models.DateTimeField(
        null=True,
    )

    last_paid_comment = models.DateTimeField()

    minimum_vote_threshold = models.BigIntegerField()

    last_delegation_check = models.DateTimeField(
        null=True,
    )

    comment_footer = models.TextField(
        null=True,
    )

    def __str__(self):
        return self.id

    class Meta:
        managed = False
        db_table = 'configuration'
