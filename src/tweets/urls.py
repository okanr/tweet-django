from django.urls import re_path
from .views import (TweetCreateView,
                    TweetListView,
                    TweetDetailView,
                    TweetUpdateView)

urlpatterns = [
    re_path('^$', TweetListView.as_view(), name='list'),  # /tweet/
    re_path('^create/$', TweetCreateView.as_view(), name='create'),  # tweet/create/
    re_path('^(?P<pk>\d+)/$', TweetDetailView.as_view(), name='detail'), # /tweet/1/
    re_path('^(?P<pk>\d+)/update/$', TweetUpdateView.as_view(), name='update'), # /tweet/1/update
]
