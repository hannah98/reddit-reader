from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

import json, collections
from urllib import request
import praw
import logging

UA = 'redditPull: personal (non public) app to pull a specific subreddit.  V1.1'
logger = logging.getLogger(__name__)

def index(request):
    return HttpResponse("You're at the subreddit index.")

def subreddit(request,subreddit):
    r = praw.Reddit(user_agent=UA)
    sr = r.get_subreddit(subreddit)
    submissions = sr.get_hot(limit=25)
    context = { 'submissions': submissions, 'subreddit': subreddit }
    #logger.error(vars(submission))
    return render(request, 'reddit/subreddit.html', context)

def comments(request,subreddit,postid):
    r = praw.Reddit(user_agent=UA)
    submission = r.get_submission(submission_id = postid)
    context = { 'submission': submission, 'comments': submission.comments, 'subreddit': subreddit }
    return render(request, 'reddit/comments_try.html', context)
