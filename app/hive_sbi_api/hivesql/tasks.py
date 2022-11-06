import logging

from celery import (current_app,
                    states as celery_states)
from celery.exceptions import Ignore
from celery.schedules import crontab

from hive_sbi_api.core.models import (Post,
                                      Vote)
from hive_sbi_api.sbi.models import MemberHist
from hive_sbi_api.sbi.data import VOTER_ACCOUNTS
from hive_sbi_api.hivesql.models import HiveSQLComment


logger = logging.getLogger('hivesql')
app = current_app._get_current_object()


@app.task(bind=True)
def sync_post_votes(self):
    logger.info("Initializing votes sync")

    last_sync_datetime = None

    if Vote.objects.exists():
        last_sync_vote = Vote.objects.latest("time")
        last_sync_datetime = last_sync_vote.member_hist_datetime

    if last_sync_datetime:
        member_hist_qr = MemberHist.objects.filter(
            voter__in=VOTER_ACCOUNTS,
            timestamp__gt=last_sync_datetime,
        )[:1000]
    else:
        member_hist_qr = MemberHist.objects.filter(
            voter__in=VOTER_ACCOUNTS,
        )[:1000]

    new_posts_counter = 0
    votes_for_create = []

    for member_hist in member_hist_qr:
        author = member_hist.author
        permlink = member_hist.permlink
        timestamp = member_hist.timestamp
        voter = member_hist.voter

        post = Post.objects.filter(
            author=author,
            permlink=permlink,
        ).first()

        if not post:
            hivesql_comment = HiveSQLComment.objects.filter(
                author=author,
                permlink=permlink,
            ).first()

            post = Post.objects.create(
                author=hivesql_comment.author,
                permlink=hivesql_comment.permlink,
                title=hivesql_comment.title,
                created=hivesql_comment.created,
                vote_rshares=hivesql_comment.vote_rshares,
                total_payout_value=hivesql_comment.total_payout_value,
                author_rewards=hivesql_comment.author_rewards,
                active_votes=hivesql_comment.active_votes,
            )

            new_posts_counter += 1

            for vote in post.active_votes:
                if vote["voter"] in VOTER_ACCOUNTS and not Vote.objects.filter(post=post, voter=vote["voter"]):

                    member_hist_vote = MemberHist.objects.filter(
                        author=author,
                        permlink=permlink,
                        voter=vote["voter"],
                    ).first()

                    if member_hist_vote:
                        member_hist_datetime = member_hist_vote.timestamp 
                    else:
                        logger.info("Vote is not registered in the steem_ops DB")
                        member_hist_datetime = timestamp

                    votes_for_create.append(Vote(
                        post=post,
                        voter=vote["voter"],
                        weight=vote["weight"],
                        rshares=vote["rshares"],
                        percent=vote["percent"],
                        reputation=vote["reputation"],
                        time=vote["time"],
                        member_hist_datetime=member_hist_datetime,
                    ))

    Vote.objects.bulk_create(votes_for_create)

    return "Created {} posts and {} votes".format(new_posts_counter, len(votes_for_create))
