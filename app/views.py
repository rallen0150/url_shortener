from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from random import choice
from string import ascii_lowercase, ascii_uppercase, digits

from app.models import Bookmark, Click
from django.http import HttpResponseRedirect

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
    fields = ('title', 'url_page', 'description')

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.new_url = ''
        for i in range(6):
            instance.new_url += choice(ascii_lowercase + ascii_uppercase + digits)
        return super().form_valid(form)

class PageView(View):
    model = Bookmark

    def get(self, request, new_url):
        return HttpResponseRedirect(Bookmark.objects.get(new_url=new_url).url_page)
