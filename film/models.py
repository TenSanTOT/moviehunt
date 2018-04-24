# -*-coding:utf-8 -*-
from django.db import models
from author.decorators import with_author
from django.contrib.auth.models import User

@with_author
class Film(models.Model):
    name = models.CharField(max_length=190)
    description = models.TextField('description')
    cover = models.ImageField(upload_to='img/', null=True, blank=True)
    vote = models.IntegerField(default=0)
    country = models.CharField(max_length=90)
    added = models.DateTimeField(auto_now_add=True)
    show = models.BooleanField(default = True)
    like = models.ManyToManyField(User, blank=True)

    class Meta:
        ordering = ["-vote"]

    def __str__(self):
        return self.name
