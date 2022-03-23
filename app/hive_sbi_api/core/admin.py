from django.contrib import admin

from .models import Member


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
