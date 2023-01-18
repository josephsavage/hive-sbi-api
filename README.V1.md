API V1
======

V1 browsable API is available in https://api.hivesbi.com/v1/. Supports 4 different endpoints:

# Members


### List

GET request to the https://api.hivesbi.com/v1/members/ endpoint. Returns paginated list of members, with 200 items per page.

#### Example

~~~
$ curl https://api.hivesbi.com/v1/members/
~~~

Response content includes the total members count, the link to the next page, and the link to the previous page. A list called "results" cointains the 200 members for the page.

~~~
{
    "count": 13863,
    "next": "http://api.hivesbi.com/v1/members/?limit=200&offset=200",
    "previous": null,
    "results": [
        {
            "account": "ecoinstats",
            "note": null,
            "shares": 16748,
            "bonus_shares": 1675,
            "total_shares": 18423,
            "total_share_days": 16431993,
            "avg_share_age": 882.349,
            "last_comment": "2022-12-17T01:18:00Z",
            "last_post": "2023-01-18T14:46:39Z",
            "original_enrollment": "2018-09-09T16:20:39Z",
            "latest_enrollment": "2023-01-18T14:29:09Z",
            "flags": null,
            "earned_rshares": 9343743196341089,
            "subscribed_rshares": 8450477032783595,
            "curation_rshares": 1999861988382,
            "delegation_rshares": 891266301569108,
            "other_rshares": 0,
            "rewarded_rshares": 6451488022308815,
            "total_rshares": 6710300398282225,
            "estimate_rewarded": 2708.23890945172,
            "balance_rshares": 258812375973410,
            "upvote_delay": 300.0,
            "updated_at": "2023-01-18T14:46:39Z",
            "first_cycle_at": "2018-12-13T18:57:26Z",
            "last_received_vote": "2023-01-18T14:52:33Z",
            "blacklisted": null,
            "hivewatchers": false,
            "buildawhale": false,
            "skiplist": false,
            "pending_balance": 108.645593766133,
            "next_upvote_estimate": 36.2151979220443
        },
        {
            "account": "steembasicincome",
            "note": null,
            "shares": 14524,
            "bonus_shares": 0,
            "total_shares": 14524,
            "total_share_days": 14159144,
            "avg_share_age": 974.879,
            "last_comment": "2023-01-17T00:34:48Z",
            "last_post": "2019-05-20T05:28:45Z",
            "original_enrollment": "2018-10-25T13:58:54Z",
            "latest_enrollment": "2022-10-03T23:48:27Z",
            "flags": null,
            "earned_rshares": 9437240049486803,
            "subscribed_rshares": 8848497493113903,
            "curation_rshares": 588742556372914,
            "delegation_rshares": 0,
            "other_rshares": 119679476600,
            "rewarded_rshares": 577611345795858,
            "total_rshares": 9409716642482071,
            "estimate_rewarded": 242.472669222331,
            "balance_rshares": 8832105296686213,
            "upvote_delay": 300.0,
            "updated_at": "2023-01-17T00:34:48Z",
            "first_cycle_at": "2019-02-19T04:33:26Z",
            "last_received_vote": "2021-09-29T18:26:03Z",
            "blacklisted": null,
            "hivewatchers": false,
            "buildawhale": false,
            "skiplist": false,
            "pending_balance": 3707.5867046716,
            "next_upvote_estimate": 1235.86223489053
        },
    ...
    ...
    ...
    ...
    ]
~~~

The "list" endpoint supports diferent ordering filters. Ordering filters can be ascending or descending. To set a descending ordering filter, just add a "-" symbol at the begining of the filter key. To use an ordering filter, just add it as a url parameter as shown below:

Ascending ordering:

~~~
https://api.hivesbi.com/v1/members/?ordering=<filter-key>
~~~

descending ordering:

~~~
https://api.hivesbi.com/v1/members/?ordering=-<filter-key>
~~~

Supported ordering filters are:

- total_shares
- shares
- bonus_shares
- estimate_rewarded
- pending_balance
- next_upvote_estimate
- total_rshares


### Retrieve

Retrieve specific member detail. GET Request to the https://api.hivesbi.com/v1/members/{username}/ endpoint.

#### Example:

Browasable api for member with username [ecoinstant](https://api.hivesbi.com/v1/members/ecoinstant/).

~~~
$ curl https://api.hivesbi.com/users/ecoinstant/
~~~

Response content:

~~~
{
    "account": "ecoinstant",
    "note": null,
    "shares": 11513,
    "bonus_shares": 875,
    "total_shares": 12388,
    "total_share_days": 9786562,
    "avg_share_age": 790.003,
    "last_comment": "2023-01-13T02:04:45Z",
    "last_post": "2023-01-09T20:54:30Z",
    "original_enrollment": "2017-12-12T17:46:54Z",
    "latest_enrollment": "2023-01-13T19:31:42Z",
    "flags": null,
    "earned_rshares": 6067582069624312,
    "subscribed_rshares": 5378399146490044,
    "curation_rshares": 34423069679682,
    "delegation_rshares": 654759853454600,
    "other_rshares": 12078245728126,
    "rewarded_rshares": 4849690081313447,
    "total_rshares": 5493007166275010,
    "estimate_rewarded": 2035.82791002297,
    "balance_rshares": 643317084961563,
    "upvote_delay": 300.0,
    "updated_at": "2023-01-13T02:04:45Z",
    "first_cycle_at": "2018-12-13T18:57:26Z",
    "last_received_vote": "2022-12-27T15:33:42Z",
    "blacklisted": null,
    "hivewatchers": false,
    "buildawhale": false,
    "skiplist": false,
    "pending_balance": 270.054963224508,
    "next_upvote_estimate": 90.0183210748361
}
~~~

# Transactions

### List

GET request to the https://api.hivesbi.com/v1/transactions/ endpoint. Returns paginated list of transactions, with 200 items per page.

#### Example

~~~
$ curl https://api.hivesbi.com/v1/transactions/
~~~

Response content includes the total transactions count, the link to the next page, and the link to the previous page. A list called "results" cointains the 200 transactions for the page.

~~~
{
    "count": 70500,
    "next": "http://api.hivesbi.com/v1/transactions/?limit=200&offset=200",
    "previous": null,
    "results": [
        {
            "index": 1163875,
            "source": "steembasicincome",
            "memo": "'@trucklife-family'",
            "account": "tengolotodo",
            "sponsor": "tengolotodo",
            "sponsees": [
                {
                    "account": "trucklife-family",
                    "units": 1
                }
            ],
            "shares": 1,
            "vests": 0.0,
            "timestamp": "2023-01-18T16:40:21Z",
            "status": "Valid",
            "share_type": "Standard"
        },
        {
            "index": 1163845,
            "source": "steembasicincome",
            "memo": "'yeckingo1'",
            "account": "ecoinstats",
            "sponsor": "ecoinstats",
            "sponsees": [
                {
                    "account": "yeckingo1",
                    "units": 1
                }
            ],
            "shares": 1,
            "vests": 0.0,
            "timestamp": "2023-01-18T14:29:09Z",
            "status": "Valid",
            "share_type": "Standard"
        },
        ...
        ...
        ...
    ]
}
~~~

Results can be filtered by different fields. Supported filters are:

- source
- account
- sponsor
- status
- share_type
- sponsee


To use filter, add these as GET parameters in the url (take a look to the 'Filters' button in the browsable API to test them), as shown below:

https://api.hivesbi.com/v1/transactions/?source=steembasicincome&account=ecoinstant


# Posts

### List

GET request to the https://api.hivesbi.com/v1/posts/ endpoint. Returns paginated list of posts voted by the SBI accounts, with 200 items per page.


#### Example

~~~
$ curl https://api.hivesbi.com/v1/posts/
~~~

Response content includes the total posts count, the link to the next page, and the link to the previous page. A list called "results" cointains the 200 posts for the page.

~~~
{
    "count": 1351205,
    "next": "http://api.hivesbi.com/v1/posts/?limit=200&offset=200",
    "previous": null,
    "results": [
        {
            "id": 817924,
            "author": "silviabeneforti",
            "permlink": "woman-at-work-",
            "title": "Woman at work ^_^",
            "created": "2017-06-18T16:21:51Z",
            "vote_rshares": 0,
            "total_payout_value": 70.34,
            "author_rewards": 33180.0,
            "total_rshares": 4068132030358,
            "hbd_rewards": 0.0,
            "hive_power_rewards": 0.0,
            "vote_set": [
                {
                    "voter": "sbi6",
                    "weight": 0,
                    "rshares": 0,
                    "percent": 100,
                    "reputation": 3375990420,
                    "time": "2018-07-09T19:50:42Z",
                    "hbd_rewards": 0.0,
                    "hive_power_rewards": 0.0
                }
            ]
        },
        {
            "id": 664209,
            "author": "nokodemion",
            "permlink": "the-attribution-problem-in-cyber-attacks",
            "title": "The Attribution Problem in Cyber Attacks",
            "created": "2017-11-10T18:59:15Z",
            "vote_rshares": 6312223497,
            "total_payout_value": 0.0,
            "author_rewards": 0.0,
            "total_rshares": 6312223497,
            "hbd_rewards": 0.0,
            "hive_power_rewards": 0.0,
            "vote_set": [
                {
                    "voter": "steembasicincome",
                    "weight": 386,
                    "rshares": 50614054,
                    "percent": 100,
                    "reputation": 0,
                    "time": "2017-11-17T01:11:33Z",
                    "hbd_rewards": 0.0,
                    "hive_power_rewards": 0.0
                }
            ]
        },
        ...
        ...
        ...
    ]
}
~~~

Results can be filtered by the author field:

https://api.hivesbi.com/v1/posts/?author=ecoinstant

Also ordered filtering by the "created" field is supported:

Ascending:

https://api.hivesbi.com/v1/posts/?author=ecoinstant&ordering=created

Descending:

https://api.hivesbi.com/v1/posts/?author=ecoinstant&ordering=-created


# Hive per mvest

### List

GET request to the https://api.hivesbi.com/v1/hive-per-mvest/ endpoint. Returns paginated list of maximum daily hive per mvest, with 200 items per page.


#### Example

~~~
$ curl https://api.hivesbi.com/v1/hive-per-mvest/
~~~

Response content includes the total hive per mvest count, the link to the next page, and the link to the previous page. A list called "results" cointains the 200 hive per mvest for the page.

~~~
{
    "count": 2473,
    "next": "http://api.hivesbi.com/v1/hive-per-mvest/?limit=200&offset=200",
    "previous": null,
    "results": [
        {
            "timestamp": "2016-04-10T13:45:45Z",
            "hivesql_id": 3,
            "block_num": 479660,
            "hive_per_mvest": 26817752596.7894
        },
        {
            "timestamp": "2016-04-11T13:45:45Z",
            "hivesql_id": null,
            "block_num": null,
            "hive_per_mvest": null
        },
        ...
        ...
        ...
    ],
}
~~~

It is possible to get the value for a specific day adding the "timestamp" filter as url parameter:


Ordered filtering by the "timestamp" field is supported:

Ascending:

https://api.hivesbi.com/v1/hive-per-mvest/?ordering=timestamp

Descending:

https://api.hivesbi.com/v1/hive-per-mvest/?ordering=-timestamp
