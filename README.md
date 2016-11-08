# RedditReader

The *very* beginnings of a web-based reader for reddit.  Blatent use of reddit stylesheets.


This is intended for personal use - it is not for public use.

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

If you are running in docker, you will want to mount the directory that contains the ```local_settings.py``` file:

```
docker run -d  -p 80:8000 -v $PWD/reddit-reader:/app/customsettings --name=reddit-reader furiousgeorge/reddit-reader
```
