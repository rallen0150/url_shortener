from django.shortcuts import render

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login

from django.views import View
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, FormView
from django.urls import reverse_lazy

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

class UserCreateView(FormView):
    template_name = "auth/user_form.html"
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('url_view')

    def form_valid(self, form):
      #save the new user first
      form.save()
      #get the username and password
      username = self.request.POST['username']
      password = self.request.POST['password1']
      #authenticate user then login
      user = authenticate(username=username, password=password)
      login(self.request, user)
      return super(UserCreateView, self).form_valid(form)

class URLCreateView(CreateView):
    model = Bookmark
    success_url = reverse_lazy('url_view')
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
    success_url = reverse_lazy('url_view')
    fields = ('title', 'description', 'public')
