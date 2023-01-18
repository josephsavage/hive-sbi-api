API V1
======

V1 browsable API is available in https://api.hivesbi.com/v1/. Supports 4 different endpoints:

## Members

## List

GET request to the https://api.hivesbi.com/v1/members/ endpoint. Returns paginated list of members, with 200 items per page.

### Example

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

The list verb supports diferent ordering filters. Ordering filters can be ascending or descending. To set a descending ordering filter, just add a "-" symbol at the begining of the filter key. To use an ordering filter, just add it as a url parameter as shown below:

Ascending ordering:

~~~
https://api.hivesbi.com/v1/members/?ordering=<filter-key>
~~~

descending ordering:

~~~
https://api.hivesbi.com/v1/members/?ordering=-<filter-key>
~~~
