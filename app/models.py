from django.db import models
from django.contrib.auth.models import User
from random import choice
from string import ascii_lowercase, ascii_uppercase, digits

# Create your models here.
class Bookmark(models.Model):
    title = models.CharField(max_length=100)
    url_page = models.URLField(null=True, blank=True)
    description = models.CharField(max_length=150, null=True, blank=True)
    created = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User)

    @property
    def new_url(self):
        key = ''
        for i in range(6):
            self.title += choice(ascii_lowercase + ascii_uppercase + digits)
        return self.title

    def __str__(self):
        return self.url_page

class Click(models.Model):
    timestamp = models.DateTimeField(auto_now=True)
    bookmark = models.ForeignKey('app.Bookmark')

    class Meta:
        ordering = ("-timestamp", )
