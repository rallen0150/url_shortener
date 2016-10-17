from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User

from app.models import Bookmark, Click

# Create your views here.

class URLView(ListView):
    model = Bookmark

class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = "/"

class URLCreateView(CreateView):
    model = Bookmark
    success_url = "/"
    fields = ('url_page', 'description')

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        # instance.bookmark = Bookmark.objects.get(id=self.kwargs['pk'])
        return super().form_valid(form)
