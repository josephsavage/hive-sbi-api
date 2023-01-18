API V0
======

V0 supports only one endpoint to get members information. Clients must send a get request to https://api.hivesbi.com/users/{member-username}/.

### Example:


Browasable api for member with username [ecoinstant](https://api.hivesbi.com/users/ecoinstant/).

~~~
$ curl https://api.hivesbi.com/users/ecoinstant/
~~~

Response content:

~~~
{
    "success": true,
    "data": {
        "username": "ecoinstant",
        "note": null,
        "shares": 11513,
        "bonusShares": 875,
        "totalShares": 12388,
        "balanceRShares": 643317084961563,
        "subscribedRShares": 5378399146490044,
        "curationRShares": 34423069679682,
        "delegationRShares": 654759853454600,
        "otherRShares": 12078245728126,
        "totalRShares": 5493007166275010,
        "rewardedRShares": 4849690081313447,
        "commentUpvote": false,
        "estimateBalanceValue": 270.054963224508,
        "estimatedNextVote": 90.0183210748361,
        "estimateRewarded": 2035.82791002297,
        "blacklisted": null,
        "skiplisted": false
    },
    "status": {
        "lastUpdatedTime": "2023-01-18T15:39:12.735640Z",
        "estimatedMinutesUntilNextUpdate": 122
    }
}
~~~
