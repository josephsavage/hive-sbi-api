from django.db import models


class Member(models.Model):
    account = models.CharField(
        unique=True,
        max_length=50,
    )

    note = models.TextField(
        blank=True,
        null=True,
    )

    shares = models.PositiveIntegerField()
    bonus_shares = models.PositiveIntegerField()

    total_share_days = models.PositiveIntegerField(
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
        blank=True,
        null=True,
    )

    earned_rshares = models.PositiveBigIntegerField(
        null=True,
    )

    subscribed_rshares = models.PositiveBigIntegerField(
        default=0,
    )

    curation_rshares = models.PositiveBigIntegerField(
        default=0,
    )

    delegation_rshares = models.PositiveBigIntegerField(
        default=0,
    )

    other_rshares = models.PositiveBigIntegerField(
        default=0,
    )

    rewarded_rshares = models.PositiveBigIntegerField(
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

    hivewatchers = models.BooleanField()
    buildawhale = models.BooleanField()

    def __str__(self):
        return self.account

    class Meta:
        verbose_name = 'member'
        verbose_name_plural = 'members'
