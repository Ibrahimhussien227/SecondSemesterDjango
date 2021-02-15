from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Users(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=20, null=True, blank=True)
    lastName = models.CharField(max_length=20, null=True, blank=True)
    email = models.CharField(max_length=20, null=True, blank=True)


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    friends = models.ManyToManyField("Profile", blank=True)
    image = models.ImageField()
    bio = models.CharField(max_length=300, blank=True)


class Post(models.Model):
    number_of_like = models.IntegerField(null=True)
    number_of_comments = models.IntegerField(null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)


class FriendRequest(models.Model):
    to_user = models.ForeignKey(User, on_delete=models.CASCADE)
    from_user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now=True)


class DeletePost(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
