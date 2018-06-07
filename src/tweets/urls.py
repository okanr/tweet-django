from django.urls import re_path
from .views import TweetListView, TweetDetailView

urlpatterns = [
    re_path('^$', TweetListView.as_view(), name='list'),  # /tweet/
    re_path('^1/$', TweetDetailView.as_view(), name='detail'),  # /tweet/1/
]
