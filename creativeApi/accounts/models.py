from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class UserProfile(models.Model):
    '''
    the created model shows info about when the person started following the user
    '''
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    bio = models.TextField()
    following = models.ManyToManyField(User, related_name="user_following", blank=True)
    followers = models.ManyToManyField(User, related_name="user_followers", blank=True)

    def __str__(self):
        return '{}"s profile'.format(self.user.username)