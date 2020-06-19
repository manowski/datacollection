# TikTok Data Collection

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

TikTok data collection including data like username, profile image, followers, likes, video content and stats about it and much more. All data are stored in PostgresQL.

Sample Demo:
[https://datainfluencer.herokuapp.com/users](https://datainfluencer.herokuapp.com/users)

### Tech

This project uses a number of open source projects to work properly:

* Flask
* PostgresQL
* aiohttp

### Endpoints
Store top 200 users by followers number
```sh
/users
```

Store all information about user
```sh
/users/<user_name>
```

Store top 200 users by country

```sh
/top/country/<country_alias>
```


License
----

MIT