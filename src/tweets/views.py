from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Tweet


# Create your views here.

class TweetListView(ListView):
    queryset = Tweet.objects.all()

    def get_context_data(self, **kwargs):
        context = super(TweetListView, self).get_context_data(**kwargs)
        return context


class TweetDetailView(DetailView):
    queryset = Tweet.objects.all()

    def get_object(self, queryset=None):
        return Tweet.objects.get(id=1)


# Retrieve
# def tweet_detail_view(request, id=1):
#     obj = Tweet.objects.get(id=id)  # GET from database
#     print(obj)
#     context = {
#         "object": obj
#     }
#     return render(request, 'tweets/detail_view.html', context)
#
#
# def tweet_list_view(request):
#     queryset = Tweet.objects.all()
#     print(queryset)
#     for obj in queryset:
#         print(obj.content)
#     context = {
#         "object_list": queryset
#     }
#     return render(request, 'tweets/list_view.html', context)
