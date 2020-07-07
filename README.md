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

Running via docker, with no customizations

```
docker run -d  -p 80:8000 --name=reddit-reader furiousgeorge/reddit-reader
```

This alone will probably not work since your reddit credentials will not be applied.  To use the reddit credentials in your praw.ini file, run the following docker command:

```
docker run -d  -p 80:8000 -v $PWD/praw.ini:/app/praw.ini --name=reddit-reader furiousgeorge/reddit-reader
```

## Customize Settings

You should modify the ```customsettings/local_settings.py``` file to change the ```ALLOWED_HOSTS``` and ```SECRET_KEY``` settings.

The default ```customsettings/local_settings.py``` file looks like this:

```
ALLOWED_SUBREDDITS = [
    'selfhosted',
    'homelab',
    'pfsense',
]

ALLOWED_HOSTS = ['localhost']

SECRET_KEY = 'CHANGE ME'
```

The ```ALLOWED_SUBREDDITS``` array contains a comma separated list of subreddits.  Each subreddit name must be enclosed in single quotes.

See the [Django Documentation](https://docs.djangoproject.com/en/3.0/ref/settings/#allowed-hosts) for the description of the ```ALLOWED_HOSTS``` setting.

See the [Django Documentation](https://docs.djangoproject.com/en/3.0/ref/settings/#secret-key) for the description of the ```SECRET_KEY``` setting.


If you are running in docker, you will want to mount the directory that contains the ```local_settings.py``` file (as well as your credentials in the praw.ini file):

```
docker run -d  -p 80:8000 -v $PWD/customsettings:/app/customsettings -v $PWD/praw.ini:/app/praw.ini --name=reddit-reader furiousgeorge/reddit-reader
```



