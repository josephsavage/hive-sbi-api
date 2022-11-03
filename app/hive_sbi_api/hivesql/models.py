from django.db import models


class HiveSQLManager(models.Manager):
    def __init__(self):
        super().__init__()
        self._db = 'hivesql'


class HiveSQLComment(models.Model):
    objects = HiveSQLManager()

    author = models.CharField(max_length=50)
    permlink = models.CharField(max_length=512)
    title = models.TextField()
    created = models.DateTimeField()
    vote_rshares = models.BigIntegerField()
    total_payout_value = models.FloatField()
    author_rewards = models.FloatField()
    active_votes = models.JSONField()

    def __str__(self):
        return "{} - {}".format(self.permlink, self.author)

    class Meta:
        managed = False
        db_table = 'Comments'


class HiveSQLTxVotes(models.Model):
    objects = HiveSQLManager()

    voter = models.CharField(
        max_length=50,
    )

    author = models.CharField(
        max_length=50,
    )

    permlink = models.CharField(
        max_length=512,
    )

    weight = models.SmallIntegerField()
    timestamp = models.DateTimeField()
    tx_id = models.BigIntegerField()

    def __str__(self):
        return "{} - {}".format(self.tx_id, self.weight)

    class Meta:
        managed = False
        db_table = 'TxVotes'
