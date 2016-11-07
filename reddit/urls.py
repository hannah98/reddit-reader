from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<subreddit>[^/]+)/$', views.subreddit, name='subreddit'),
    url(r'^(?P<subreddit>[^/]+)/comments/(?P<postid>[^/]+)', views.comments, name='comments'),
]
