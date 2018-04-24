from django.db import models
from author.decorators import with_author
from django.contrib.auth.models import User

@with_author
class Comment(models.Model):
    film = models.ForeignKey('film.Film', related_name='comment', on_delete=models.CASCADE)
    text = models.TextField()
    added = models.DateTimeField(auto_now_add=True)
    approved_comment = models.BooleanField(default=True)

    def __str__(self):
        return self.text

    class Meta:
        ordering=['-added']
