from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

import json, collections
from urllib import request
import praw
import logging
from . import get_allowed_subreddits

#from django.conf import settings

UA = 'redditPull: personal (non public) app to pull a specific subreddit.  V1.1'
logger = logging.getLogger(__name__)
allowed_subreddits = get_allowed_subreddits()

def index(request):
    #return HttpResponse("You're at the subreddit index.")
    context = { 'title': 'Reddit Reader Home', 'allowed_subreddits': allowed_subreddits  }
    return render(request, 'reddit/index.html', context)

def subreddit(request,subreddit):
    r = praw.Reddit(user_agent=UA)
    sr = r.get_subreddit(subreddit)
    submissions = sr.get_hot(limit=25)
    
    context = { 'submissions': submissions, 'subreddit': subreddit, 'allowed_subreddits': allowed_subreddits }
    #logger.error(vars(submission))
    if is_subreddit_allowed(subreddit):
        logger.error("Subreddit allowed")
    else:
        logger.error("Subreddit NOT allowed")
        
    return render(request, 'reddit/subreddit.html', context)

def comments(request,subreddit,postid):
    r = praw.Reddit(user_agent=UA)
    submission = r.get_submission(submission_id = postid)
    context = { 'submission': submission, 'comments': submission.comments, 'subreddit': subreddit, 'allowed_subreddits': allowed_subreddits }
    return render(request, 'reddit/comments.html', context)

def is_subreddit_allowed(subreddit):
    if allowed_subreddits:
        if subreddit not in allowed_subreddits:
            return False
    return True
