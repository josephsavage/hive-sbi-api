from django.utils.translation import gettext_lazy as _

SOURCE_MGMT = 'mgmt'
SOURCE_STEEM_BASIC_INCOME = 'steembasicincome'
SOURCE_SBI_10 = 'sbi10'
SOURCE_SBI_9 = 'sbi9'
SOURCE_SBI_8 = 'sbi8'
SOURCE_SBI_7 = 'sbi7'
SOURCE_SBI_6 = 'sbi6'
SOURCE_SBI_5 = 'sbi5'
SOURCE_SBI_4 = 'sbi4'
SOURCE_SBI_3 = 'sbi3'
SOURCE_SBI_2 = 'sbi2'
SOURCE_SHARES = 'shares'

# tomorrow.strftime('%a')
TRX_SOURCE_CHOICES = (
    (SOURCE_MGMT, _('mgmt')),
    (SOURCE_STEEM_BASIC_INCOME, _('steembasicincome')),
    (SOURCE_SBI_10, _('sbi10')),
    (SOURCE_SBI_9, _('sbi9')),
    (SOURCE_SBI_8, _('sbi8')),
    (SOURCE_SBI_7, _('sbi7')),
    (SOURCE_SBI_6, _('sbi6')),
    (SOURCE_SBI_5, _('sbi5')),
    (SOURCE_SBI_4, _('sbi4')),
    (SOURCE_SBI_3, _('sbi3')),
    (SOURCE_SBI_2, _('sbi2')),
    (SOURCE_SHARES, _('shares')),
)


STATUS_VALID = 'Valid'
STATUS_REFUNDED = 'Refunded'
STATUS_ACCOUNT_DOES_NOT_EXISTS = 'AccountDoesNotExist'
STATUS_REFUSED = 'Refused'
STATUS_LESS_OR_NO_SPONSEE = 'LessOrNoSponsee'


TRX_STATUS_CHOICES = (
    (STATUS_VALID, _('Valid')),
    (STATUS_REFUNDED, _('Refunded')),
    (STATUS_ACCOUNT_DOES_NOT_EXISTS, _('AccountDoesNotExist')),
    (STATUS_REFUSED, _('Refused')),
    (STATUS_LESS_OR_NO_SPONSEE, _('LessOrNoSponsee')),
) 

SHARE_TYPE_MGMT = 'Mgmt'
SHARE_TYPE_STANDARD = 'Standard'
SHARE_TYPE_DELEGATION = 'Delegation'
SHARE_TYPE_SBD = 'SBD'
SHARE_TYPE_REFUND = 'Refund'
SHARE_TYPE_REMOVED_DELEGATION = 'RemovedDelegation'
SHARE_TYPE_DELEGATION_LEASED = 'DelegationLeased'
SHARE_TYPE_REFUNDED = 'Refunded'
SHARE_TYPE_MGMT_TRANSFER = 'MgmtTransfer'
SHARE_TYPE_SHARE_TRANSFER = 'ShareTransfer'
SHARE_TYPE_HBD = 'HBD'


TRX_SHARE_TYPE_CHOICES = (
    (SHARE_TYPE_MGMT, _('Mgmt')),
    (SHARE_TYPE_STANDARD, _('Standard')),
    (SHARE_TYPE_DELEGATION, _('Delegation')),
    (SHARE_TYPE_SBD, _('SBD')),
    (SHARE_TYPE_REFUND, _('Refund')),
    (SHARE_TYPE_REMOVED_DELEGATION, _('RemovedDelegation')),
    (SHARE_TYPE_DELEGATION_LEASED, _('DelegationLeased')),
    (SHARE_TYPE_REFUNDED, _('Refunded')),
    (SHARE_TYPE_MGMT_TRANSFER, _('MgmtTransfer')),
    (SHARE_TYPE_SHARE_TRANSFER, _('ShareTransfer')),
    (SHARE_TYPE_HBD, _('HBD')),
)


FAILED_TRX_TYPE_NO_ACCOUNT = 1
FAILED_TRX_TYPE_NO_SPONSOR = 2
FAILED_TRX_TYPE_EMPTY_SPONSEE = 3
FAILED_TRX_TYPE_NO_SPONSEE_ACCOUNT = 4
FAILED_TRX_TYPE_BAD_SPONSEE_FORMAT = 5


FAILED_TRX_TYPE_CHOICES = (
    (FAILED_TRX_TYPE_NO_ACCOUNT, _('Account does not exist')),
    (FAILED_TRX_TYPE_NO_SPONSOR, _('Sponsor does not exist')),
    (FAILED_TRX_TYPE_EMPTY_SPONSEE, _('Empty sponsee')),
    (FAILED_TRX_TYPE_NO_SPONSEE_ACCOUNT, _('Sponsee acount does not exist')),
    (FAILED_TRX_TYPE_BAD_SPONSEE_FORMAT, _('Bad sponsee format')),
)
