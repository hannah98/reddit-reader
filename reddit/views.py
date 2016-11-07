from django.shortcuts import render
from django.template import loader

# Create your views here.
from django.http import HttpResponse
#import html

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
    context = { 'submissions': submissions }
    #logger.error(vars(submission))
    return render(request, 'reddit/subreddit.html', context)
        
    #return HttpResponse("Subreddit %s: %s" % subreddit,j)

def comments(request,subreddit,postid):
    r = praw.Reddit(user_agent=UA)
    submission = r.get_submission(submission_id = postid)
    flat_comments = submission.comments
    context = { 'submission': submission, 'comments': flat_comments, 'title': submission.title }
    return render(request, 'reddit/comments_try.html', context)
    

def comments_flat(request,subreddit,postid):
    r = praw.Reddit(user_agent=UA)
    submission = r.get_submission(submission_id = postid)
    flat_comments = praw.helpers.flatten_tree(submission.comments)
    #logger.error(vars(flat_comments[1]))
    #logger.error(json.dumps(submission.comments.__dict__))
    context = { 'submission': submission, 'comments': flat_comments }
    return render(request, 'reddit/comments.html', context)

