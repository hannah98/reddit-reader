from django.conf import settings

def get_allowed_subreddits():
    if hasattr(settings, 'ALLOWED_SUBREDDITS'):
        return settings.ALLOWED_SUBREDDITS
    else:
        return None
