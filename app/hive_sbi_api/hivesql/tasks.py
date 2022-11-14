import logging
import pytz

from datetime import (datetime,
                      timedelta)

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


@app.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
        crontab(minute=30, hour='*/1'),
        sync_post_votes.s(),
        name='sync_post_votes',
    )


@app.task(bind=True)
def sync_empty_votes_posts(self):
    empty_votes_posts = Post.objects.filter(
        vote=None,
        empty_votes=False,
    )

    empty_votes_posts_counter = 0
    synchronized_posts = 0

    for post in empty_votes_posts:
        votes_for_create = []

        for vote in post.active_votes:
            if vote["voter"] in VOTER_ACCOUNTS and not Vote.objects.filter(post=post, voter=vote["voter"]):
                member_hist_vote = MemberHist.objects.filter(
                    author=post.author,
                    permlink=post.permlink,
                    voter=vote["voter"],
                ).first()

                if member_hist_vote:
                    member_hist_datetime = member_hist_vote.timestamp
                else:
                    member_hist_datetime = post.created

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

        if not votes_for_create:
            post.empty_votes = True
            post.save()

            empty_votes_posts_counter += 1

            continue

        Vote.objects.bulk_create(votes_for_create)
        synchronized_posts += 1

    return "Found {} posts without votes. {} posts synchronized.".format(
        empty_votes_posts_counter,
        synchronized_posts,
    )


@app.task(bind=True)
def sync_post_votes(self):
    logger.info("Initializing votes sync")

    last_sync_datetime = None

    if Vote.objects.exists():
        last_sync_vote = Vote.objects.latest("time")
        last_sync_datetime = last_sync_vote.member_hist_datetime

    timestamp_limit = datetime.now() - timedelta(days=7)
    timestamp_limit = timestamp_limit.replace(tzinfo=pytz.UTC)

    if last_sync_datetime:
        member_hist_qr = MemberHist.objects.filter(
            voter__in=VOTER_ACCOUNTS,
            timestamp__gt=last_sync_datetime,
            timestamp__lt=timestamp_limit,
        )[:1500]
    else:
        member_hist_qr = MemberHist.objects.filter(
            voter__in=VOTER_ACCOUNTS,
            timestamp__lt=timestamp_limit,
        )[:1500]

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
            new_posts_counter += 1

            hivesql_comment = HiveSQLComment.objects.filter(
                author=author,
                permlink=permlink,
            ).first()

            if not hivesql_comment:
                continue

            post = Post.objects.create(
                author=hivesql_comment.author,
                permlink=hivesql_comment.permlink,
                title=hivesql_comment.title,
                created=hivesql_comment.created,
                vote_rshares=hivesql_comment.vote_rshares,
                total_payout_value=hivesql_comment.total_payout_value,
                author_rewards=hivesql_comment.author_rewards,
                active_votes=hivesql_comment.active_votes,
                total_rshares=0,
            )

            total_rshares = 0

            for vote in post.active_votes:
                total_rshares = total_rshares + int(vote["rshares"])

                if vote["voter"] in VOTER_ACCOUNTS and not Vote.objects.filter(post=post, voter=vote["voter"]):

                    member_hist_vote = MemberHist.objects.filter(
                        author=author,
                        permlink=permlink,
                        voter=vote["voter"],
                    ).first()

                    if member_hist_vote:
                        member_hist_datetime = member_hist_vote.timestamp 
                    else:
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

            post.total_rshares = total_rshares
            post.save()

    Vote.objects.bulk_create(votes_for_create)
    sync_empty_votes_posts.delay()

    return "Created {} posts and {} votes".format(new_posts_counter, len(votes_for_create))
