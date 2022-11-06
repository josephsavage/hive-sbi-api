import json
import logging
import requests

from datetime import datetime
from datetime import timedelta

from celery import (current_app,
                    states as celery_states)
from celery.exceptions import Ignore
from celery.schedules import crontab
from django_celery_results.models import TaskResult

from django.db.utils import IntegrityError
from django.forms.models import model_to_dict

from hive_sbi_api.sbi.models import (SBIMember,
                                     SBIConfiguration,
                                     SBITransaction)
from hive_sbi_api.core.models import (Member,
                                      Configuration,
                                      Transaction,
                                      Sponsee,
                                      FailedTransaction)

from hive_sbi_api.core.data import (FAILED_TRX_TYPE_NO_ACCOUNT,
                                    FAILED_TRX_TYPE_NO_SPONSOR,
                                    FAILED_TRX_TYPE_EMPTY_SPONSEE,
                                    FAILED_TRX_TYPE_NO_SPONSEE_ACCOUNT,
                                    FAILED_TRX_TYPE_BAD_SPONSEE_FORMAT,
                                    FAILED_TRX_NOT_SYNCED_ACCOUNT,
                                    FAILED_TRX_NOT_SYNCED_SPONSOR)

from hive_sbi_api.core.serializers import SBITransactionSerializer

from hive_sbi_api.hivesql.tasks import sync_post_votes


logger = logging.getLogger('sbi')

app = current_app._get_current_object()

@app.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
        crontab(hour=18, minute=0),
        sync_members.s(),
        name='sync members_18',
    )

    sender.add_periodic_task(
        crontab(hour=20, minute=24),
        sync_members.s(),
        name='sync members_20',
    )

    sender.add_periodic_task(
        crontab(hour=22, minute=48),
        sync_members.s(),
        name='sync members_22',
    )

    sender.add_periodic_task(
        crontab(hour=1, minute=12),
        sync_members.s(),
        name='sync members_1',
    )

    sender.add_periodic_task(
        crontab(hour=3, minute=36),
        sync_members.s(),
        name='sync members_3',
    )

    sender.add_periodic_task(
        crontab(hour=6, minute=0),
        sync_members.s(),
        name='sync members_6',
    )

    sender.add_periodic_task(
        crontab(hour=8, minute=24),
        sync_members.s(),
        name='sync members_8',
    )


    sender.add_periodic_task(
        crontab(hour=10, minute=48),
        sync_members.s(),
        name='sync members_10',
    )

    sender.add_periodic_task(
        crontab(hour=13, minute=12),
        sync_members.s(),
        name='sync members_13',
    )

    sender.add_periodic_task(
        crontab(hour=15, minute=36),
        sync_members.s(),
        name='sync members_15',
    )

    sender.add_periodic_task(
        crontab(hour=1, minute=30, day_of_week=1),
        clean_task_results.s(),
        name='clean_task_results',
    )


@app.task(bind=True)
def sync_trx(self):
    pending_transactions = SBITransaction.objects.all()

    if Transaction.objects.count():
        pending_transactions = SBITransaction.objects.filter(
            timestamp__gt=Transaction.objects.latest("timestamp").timestamp
        )

    created_transactions = 0
    failed_transactions = 0

    for pending_trx in pending_transactions:
        index = pending_trx.index
        sponsee = pending_trx.sponsee
        trx = None

        pending_trx_data = SBITransactionSerializer(pending_trx).data
        pending_trx_account = pending_trx.account.strip()
        pending_trx_sponsor = pending_trx.sponsor.strip()

        account = Member.objects.filter(account=pending_trx_account).first()

        if not account:
            account = SBIMember.objects.filter(account=pending_trx_account).first()

            if account:
                FailedTransaction.objects.create(
                    transaction=trx,
                    trx_index=index,
                    fail_type=FAILED_TRX_NOT_SYNCED_ACCOUNT,
                    description="Not synced account",
                    trx_data=pending_trx_data,
                    spoonse_text=sponsee,
                    share_type=pending_trx.share_type,
                    status=pending_trx.status,
                    account=pending_trx_account,
                    sponsor=pending_trx_sponsor,
                )

            else:
                FailedTransaction.objects.create(
                    transaction=trx,
                    trx_index=index,
                    fail_type=FAILED_TRX_TYPE_NO_ACCOUNT,
                    description="Account does not exist",
                    trx_data=pending_trx_data,
                    spoonse_text=sponsee,
                    share_type=pending_trx.share_type,
                    status=pending_trx.status,
                    account=pending_trx_account,
                    sponsor=pending_trx_sponsor,
                )

            failed_transactions += 1

            continue

        sponsor = Member.objects.filter(account=pending_trx_sponsor).first()

        if not sponsor:
            sponsor = SBIMember.objects.filter(account=pending_trx_sponsor).first()

            if sponsor:
                FailedTransaction.objects.create(
                    transaction=trx,
                    trx_index=index,
                    fail_type=FAILED_TRX_NOT_SYNCED_SPONSOR,
                    description="Not synced sponsor",
                    trx_data=pending_trx_data,
                    spoonse_text=sponsee,
                    share_type=pending_trx.share_type,
                    status=pending_trx.status,
                    account=pending_trx_account,
                    sponsor=pending_trx_sponsor,
                )

            else:
                FailedTransaction.objects.create(
                    transaction=trx,
                    trx_index=index,
                    fail_type=FAILED_TRX_TYPE_NO_SPONSOR,
                    description="Sponsor does not exist",
                    trx_data=pending_trx_data,
                    spoonse_text=sponsee,
                    share_type=pending_trx.share_type,
                    status=pending_trx.status,
                    account=pending_trx_account,
                    sponsor=pending_trx_sponsor,
                )

            failed_transactions += 1

            continue

        trx = Transaction.objects.create(
            index=index,
            source=pending_trx.source,
            memo=pending_trx.memo,
            account=account,
            sponsor=sponsor,
            shares=pending_trx.shares,
            vests=pending_trx.vests,
            timestamp=pending_trx.timestamp,
            status=pending_trx.status,
            share_type=pending_trx.share_type,
        )  

        created_transactions += 1

        if sponsee:
            try:
                sponsee_dict = json.loads(sponsee)

                for sponsee_account, units in sponsee_dict.items():
                    if Member.objects.filter(account=sponsee_account):
                        Sponsee.objects.create(
                            trx=trx,
                            account=Member.objects.filter(account=sponsee_account).first(),
                            units=units,
                        )

                    else:
                        if not FailedTransaction.objects.filter(
                            transaction=trx,
                            trx_index=index,
                            fail_type=FAILED_TRX_TYPE_NO_SPONSEE_ACCOUNT,
                        ):
                            FailedTransaction.objects.create(
                                trx_index=index,
                                transaction=trx,
                                fail_type=FAILED_TRX_TYPE_NO_SPONSEE_ACCOUNT,
                                description="Spoonse account does not exist",
                                trx_data=pending_trx_data,
                                spoonse_text=sponsee,
                                share_type=pending_trx.share_type,
                                status=pending_trx.status,
                                account=pending_trx_account,
                                sponsor=pending_trx_sponsor,
                            )

                            failed_transactions += 1

            except json.decoder.JSONDecodeError as e:
                FailedTransaction.objects.create(
                    trx_index=index,
                    transaction=trx,
                    fail_type=FAILED_TRX_TYPE_BAD_SPONSEE_FORMAT,
                    description="{}".format(e),
                    trx_data=pending_trx_data,
                    spoonse_text=sponsee,
                    share_type=pending_trx.share_type,
                    status=pending_trx.status,
                    account=pending_trx_account,
                    sponsor=pending_trx_sponsor,
                )

                failed_transactions += 1
        else:
            FailedTransaction.objects.create(
                trx_index=index,
                transaction=trx,
                fail_type=FAILED_TRX_TYPE_EMPTY_SPONSEE,
                description="No sponsee info",
                trx_data=pending_trx_data,
                spoonse_text=sponsee,
                share_type=pending_trx.share_type,
                status=pending_trx.status,
                account=pending_trx_account,
                sponsor=pending_trx_sponsor,
            )

            failed_transactions += 1

            continue


    return "Created {} transactions. Failed {} transactions".format(
        created_transactions,
        failed_transactions,
    )


def sync_conf():
    sbi_conf = SBIConfiguration.objects.first()
    conf = Configuration.objects.first()

    for attr, value in model_to_dict(sbi_conf).items():
        setattr(conf, attr, value)
    conf.save()


@app.task(bind=True)
def sync_members(self):
    sync_conf()

    sbi_conf = Configuration.objects.first()

    SBImembers = SBIMember.objects.all()

    created_members = 0
    members_to_update = []

    failured_members_sync = {}

    for sbi_member in SBImembers:
        # Validate negative values FOR curation_rshares,
        # and other_rshares, rewarded_rshares.
        curation_rshares = sbi_member.curation_rshares

        if curation_rshares < 0:
            curation_rshares = 0

        other_rshares = sbi_member.other_rshares

        if other_rshares < 0:
            other_rshares = 0

        other_rshares = sbi_member.other_rshares

        if other_rshares < 0:
            other_rshares = 0

        rewarded_rshares = sbi_member.rewarded_rshares

        if rewarded_rshares < 0 or rewarded_rshares is None:
            rewarded_rshares = 0

        pending_balance = sbi_member.balance_rshares / sbi_conf.minimum_vote_threshold * 0.02
        next_upvote_estimate = pending_balance / sbi_conf.comment_vote_divider
        estimate_rewarded = rewarded_rshares / sbi_conf.minimum_vote_threshold * 0.02

        total_rshares = rewarded_rshares + sbi_member.balance_rshares

        # Validate boolean fields.
        # hivewatchers and buildawhale. 
        hivewatchers = sbi_member.hivewatchers

        if hivewatchers is None:
            hivewatchers = False

        buildawhale = sbi_member.buildawhale

        if buildawhale is None:
            buildawhale = False

        comment_upvote = sbi_member.comment_upvote

        if comment_upvote is None:
            comment_upvote = False

        data_dict = {
            'note': sbi_member.note,
            'shares': sbi_member.shares,
            'bonus_shares': sbi_member.bonus_shares,
            'total_shares': sbi_member.shares + sbi_member.bonus_shares,
            'total_share_days': sbi_member.total_share_days,
            'avg_share_age': sbi_member.avg_share_age,
            'last_comment': sbi_member.last_comment,
            'last_post': sbi_member.last_post,
            'original_enrollment': sbi_member.original_enrollment,
            'latest_enrollment': sbi_member.latest_enrollment,
            'flags': sbi_member.flags,
            'earned_rshares': sbi_member.earned_rshares,
            'subscribed_rshares': sbi_member.subscribed_rshares,
            'curation_rshares': curation_rshares,
            'delegation_rshares': sbi_member.delegation_rshares,
            'other_rshares': other_rshares,
            'rewarded_rshares': rewarded_rshares,
            'pending_balance': pending_balance,
            'next_upvote_estimate': next_upvote_estimate,
            'estimate_rewarded': estimate_rewarded,
            'balance_rshares': sbi_member.balance_rshares,
            'total_rshares': total_rshares,
            'upvote_delay': sbi_member.upvote_delay,
            'updated_at': sbi_member.updated_at,
            'first_cycle_at': sbi_member.first_cycle_at,
            'last_received_vote': sbi_member.last_received_vote,
            'blacklisted': sbi_member.blacklisted,
            'hivewatchers': hivewatchers,
            'buildawhale': buildawhale,
            'comment_upvote': comment_upvote,
        }

        try:
            obj, created = Member.objects.get_or_create(
                account=sbi_member.account,
                defaults=data_dict,
            )

            if created:
                created_members += 1
            else:
                for attr, value in data_dict.items(): 
                    setattr(obj, attr, value)
                members_to_update.append(obj)

        except IntegrityError as e:
            failured_members_sync[sbi_member.account] = "{}".format(e)
            continue

    updated_member = Member.objects.bulk_update(
        members_to_update,
        [
            'note',
            'shares',
            'bonus_shares',
            'total_shares',
            'total_share_days',
            'avg_share_age',
            'last_comment',
            'last_post',
            'latest_enrollment',
            'flags',
            'earned_rshares',
            'subscribed_rshares',
            'curation_rshares',
            'delegation_rshares',
            'other_rshares',
            'rewarded_rshares',
            'pending_balance',
            'next_upvote_estimate',
            'estimate_rewarded',
            'balance_rshares',
            'total_rshares',
            'upvote_delay',
            'updated_at',
            'first_cycle_at',
            'last_received_vote',
            'blacklisted',
            'hivewatchers',
            'buildawhale',
            'comment_upvote',
        ]
    )

    sync_trx.delay()
    sync_post_votes.delay()

    if failured_members_sync:
        self.update_state(
            state=celery_states.FAILURE,
            meta=failured_members_sync,
        )

        raise Ignore()

    return "Created {} members. Updated {} members".format(created_members, updated_member)


@app.task
def clean_task_results():
    task_results_to_delete = TaskResult.objects.filter(
        date_done__lt=datetime.now() - timedelta(days=7)
    )

    task_results_count = task_results_to_delete.count()
    task_results_to_delete.delete()

    return "Deleted {} task results".format(task_results_count)
