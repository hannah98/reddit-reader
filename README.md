# RedditReader

The *very* beginnings of a web-based reader for reddit.  Blatent use of reddit stylesheets.


This is intended for personal use - it is not for public use.

## Reddit credentials

### Reddit application

The first thing you need to do is setup a new reddit application, as described under [Script Application](http://praw.readthedocs.io/en/latest/getting_started/authentication.html#script-application) in the praw documentation.

### Praw ini file

The next thing you need to do is create a praw.ini file on your local system as described on the [praw ini files](http://praw.readthedocs.io/en/latest/getting_started/configuration/prawini.html) page of the praw documentation.

The basic format of the praw.ini file should look like this:

```
[DEFAULT]

client_id=
client_secret=
password=
username=

```

## Docker

Running via docker

```
docker run -d  -p 80:8000 --name=reddit-reader furiousgeorge/reddit-reader
```

## Whitelisting subreddits

If you want to whitelist subreddits, just add lines to the ```customsettings/local_settings.py``` file, following this format:

```
ALLOWED_SUBREDDITS = [
    'subreddit1',
    'subreddit2',
    'subreddit3',
]
```

If you are running in docker, you will want to mount the directory that contains the ```local_settings.py``` file as well as your credentials in the praw.ini file:

```
docker run -d  -p 80:8000 -v $PWD/customsettings:/app/customsettings -v $PWD/praw.ini:/app/praw.ini --name=reddit-reader furiousgeorge/reddit-reader
```
