from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.db.models import Q
from django.views.generic import (CreateView, DeleteView,
                                  DetailView, ListView, UpdateView)
from .forms import TweetModelForm
from .models import Tweet
from .mixins import FormUserNeededMixin, UserOwnerMixin


# Create your views here.


# class TweetCreateView(LoginRequiredMixin, FormUserNeededMixin, CreateView):
class TweetCreateView(FormUserNeededMixin, CreateView):
    form_class = TweetModelForm
    template_name = 'tweets/create_view.html'
    # success_url = reverse_lazy('tweet:detail')


class TweetUpdateView(LoginRequiredMixin, UserOwnerMixin, UpdateView):
    queryset = Tweet.objects.all()
    form_class = TweetModelForm
    template_name = 'tweets/update_view.html'
    # success_url = '/tweet/'


class TweetDeleteView(LoginRequiredMixin, DeleteView):
    model = Tweet
    template_name = 'tweets/delete_confirm.html'
    success_url = reverse_lazy('tweet:list')


class TweetListView(ListView):

    def get_queryset(self):
        queryset = Tweet.objects.all()
        query = self.request.GET.get('q', None)
        if query is not None:
            queryset = queryset.filter(Q(content__icontains=query) |
                                       Q(user__username__icontains=query))
        return queryset

    def get_context_data(self, **kwargs):
        context = super(TweetListView, self).get_context_data(**kwargs)
        return context


class TweetDetailView(DetailView):
    queryset = Tweet.objects.all()


def tweet_detail_view(request, pk=None):  # pk == id
    # obj = Tweet.objects.get(pk=pk) # GET from database
    obj = get_object_or_404(Tweet, pk=pk)
    print(obj)
    context = {
        "object": obj
    }
    return render(request, "tweets/detail_view.html", context)
