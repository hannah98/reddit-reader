from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

import json, collections
from urllib import request
import praw
import logging
import os
from . import get_allowed_subreddits, get_subreddit_limit, get_app_version

UA = 'redditPull: personal (non public) app to pull a specific subreddit.  V1.1'
logger = logging.getLogger(__name__)
logger.setLevel(os.getenv("LOGLEVEL", "WARNING"))
logger.error("Log Level %s", logger.level)
allowed_subreddits = get_allowed_subreddits()
subreddit_limit = get_subreddit_limit()
app_version = get_app_version()

def index(request):
    context = { 'title': 'Reddit Reader Home', 'allowed_subreddits': allowed_subreddits, 'app_version': app_version  }
    return render(request, 'reddit/index.html', context)

def subreddit(request,subreddit):
    if not is_subreddit_allowed(subreddit):
        not_allowed_context = { 'subreddit': subreddit, 'allowed_subreddits': allowed_subreddits }
        logger.error("Subreddit %s not allowed" % subreddit)
        return render(request, 'reddit/not_allowed.html', not_allowed_context)

    r = praw.Reddit(user_agent=UA)
    logger.info("Fetching %i entries from %s",subreddit_limit,subreddit)
    submissions = r.subreddit(subreddit).hot(limit=subreddit_limit)
    
    context = { 'submissions': submissions, 'subreddit': subreddit, 'allowed_subreddits': allowed_subreddits, 'app_version': app_version }
        
    return render(request, 'reddit/subreddit.html', context)

def comments(request,subreddit,postid):
    r = praw.Reddit(user_agent=UA)
    submission = r.submission(id=postid)
    context = { 'submission': submission, 'comments': submission.comments, 'subreddit': subreddit, 'allowed_subreddits': allowed_subreddits, 'app_version': app_version }
    return render(request, 'reddit/comments.html', context)

def is_subreddit_allowed(subreddit):
    if allowed_subreddits:
        if subreddit not in allowed_subreddits:
            return False
    return True
