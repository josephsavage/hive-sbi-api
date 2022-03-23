from django.contrib import admin

from .models import (Member,
                     Configuration)


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = (
        'account',
        'updated_at',
    )

    search_fields = ['account',]

    list_filter = [
        'last_comment',
        'last_post',
        'original_enrollment',
        'latest_enrollment',
        'updated_at',
        'first_cycle_at',
        'last_received_vote',
        'blacklisted',
        'hivewatchers',
        'buildawhale',
    ]


@admin.register(Configuration)
class ConfigurationAdmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    list_display = (
        'share_cycle_min',
        'sp_share_ratio',
        'rshares_per_cycle',
        'del_rshares_per_cycle',
        'comment_vote_divider',
        'comment_vote_timeout_h',
        'last_cycle',
        'upvote_multiplier',
        'upvote_multiplier_adjusted',
        'last_paid_post',
        'last_paid_comment',
        'minimum_vote_threshold',
        'last_delegation_check',
        'comment_footer',
    )
