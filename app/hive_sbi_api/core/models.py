from django.db import models


class Configuration(models.Model):
    share_cycle_min = models.FloatField(
        default=144,
    )

    sp_share_ratio = models.FloatField(
        default=2,
    )

    rshares_per_cycle = models.BigIntegerField(
        null=True,
        default=800000000,
    )

    del_rshares_per_cycle = models.BigIntegerField(
        default=800000000,
    )

    comment_vote_divider = models.FloatField(
        null=True,
    )

    comment_vote_timeout_h = models.FloatField(
        null=True,
    )

    last_cycle = models.DateTimeField(
        null=True,
    )

    upvote_multiplier = models.FloatField(
        default=1.05,
    )

    upvote_multiplier_adjusted = models.FloatField(
        default=1,
    )

    last_paid_post = models.DateTimeField(
        null=True,
    )

    last_paid_comment = models.DateTimeField()

    minimum_vote_threshold = models.BigIntegerField(
        default=800000000,
    )

    last_delegation_check = models.DateTimeField(
        null=True,
    )

    comment_footer = models.TextField(
        null=True,
    )

    def __str__(self):
        return "Configuration"

    class Meta:
        verbose_name = 'configuration'
        verbose_name_plural = 'configuration'


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

    @property
    def pending_balance(self):
        sbi_conf = Configuration.objects.first()
        return self.balance_rshares / sbi_conf.minimum_vote_threshold * 0.02

    @property
    def next_upvote_estimate(self):
        sbi_conf = Configuration.objects.first()
        return self.pending_balance / sbi_conf.comment_vote_divider

    @property
    def estimate_rewarded(self):
        sbi_conf = Configuration.objects.first()
        return self.rewarded_rshares / sbi_conf.minimum_vote_threshold * 0.02


    @property
    def skiplist(self):
        if self.blacklisted:
            skiplist = True
        elif self.blacklisted is False:
            skiplist = False
        elif self.blacklisted is None:
            if self.buildawhale or self.hivewatchers:
                skiplist = True
            else:
                skiplist = False

        return skiplist

    def __str__(self):
        return self.account

    class Meta:
        verbose_name = 'member'
        verbose_name_plural = 'members'
