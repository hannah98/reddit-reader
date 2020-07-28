from django.conf import settings

def get_allowed_subreddits():
    if hasattr(settings, 'ALLOWED_SUBREDDITS'):
        return settings.ALLOWED_SUBREDDITS
    else:
        return None

def get_subreddit_limit():
    limit = 25
    if hasattr(settings, 'SUBREDDIT_LIMIT'):
        trylimit = settings.SUBREDDIT_LIMIT
        try:
            limit = int(trylimit)
            if limit <0 or limit > 100:
                limit = 25
        except ValueError:
            pass
    return limit

def get_app_version():
    if hasattr(settings, 'VERSION'):
        return settings.VERSION
    else:
        return '1.0.unknown'
