from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views import View
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import User
from random import choice
from string import ascii_lowercase, ascii_uppercase, digits

from app.models import Bookmark, Click
from django.http import HttpResponseRedirect

# Create your views here.

class URLView(ListView):
    model = Bookmark

    def get_context_data(self):
        context = super().get_context_data()
        context['login'] = AuthenticationForm
        return context

class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = "/"

class URLCreateView(CreateView):
    model = Bookmark
    success_url = "/"
    fields = ('title', 'url_page', 'description', 'public')

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.new_url = ''
        for i in range(6):
            instance.new_url += choice(ascii_lowercase + ascii_uppercase + digits)
        return super().form_valid(form)

class PageView(View):
    def get(self, request, new_url):
        x = Bookmark.objects.get(new_url=new_url)
        Click.objects.create(bookmark=x)
        return HttpResponseRedirect(x.url_page)

class URLUpdateView(UpdateView):
    model = Bookmark
    success_url = "/"
    fields = ('title', 'description', 'public')
