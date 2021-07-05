from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from member.models import Member
from django.conf import settings


# Create your models here.

#  모든 게시판 게시물 db
class BoardAllContentList(models.Model):
    title = models.CharField(max_length=100)
    # user = models.ForeignKey(Member, on_delete=models.CASCADE) # main user db랑 연결 해야함
    user = models.CharField(max_length=20) # main user db랑 연결 해야함
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    seenum = models.IntegerField(null=True)
    # like = models.ManyToManyField(
    #     settings.AUTH_USER_MODEL, # this is preferred than just 'User'
    #     blank=True, # blank is allowed
    #     related_name='likes_user'
    # )
    like_count = models.PositiveIntegerField(default=0)
    board_kind = models.CharField(max_length=20)
<<<<<<< HEAD
    # #### 추가 ####
    # likes = models.ManyToManyField(User, related_name="like_post", blank=True)
=======

    # def count_likes_user(self): # total likes_user
    #     return self.like.count()
>>>>>>> 4c459b79fa2e74abb1044bafedaed4a4107ccf59

    def __str__(self):
        return self.title

class Profile(models.Model):
    user_name = models.CharField(max_length=20)
    # nickname = models.TextField(max_length=10)
    like_posts = models.ManyToManyField(BoardAllContentList, blank=True, related_name='like_users')


# 게시물 별 이미지 db
class Image(models.Model):
    content = models.ForeignKey(BoardAllContentList, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)


# 모든 게시판 댓글 db
class Board_comment(models.Model):
    content = models.ForeignKey(BoardAllContentList, on_delete=models.CASCADE, null=True, related_name='content')
    comment_date = models.DateTimeField(auto_now_add=True)
    # comment_writer = models.ForeignKey(Member,on_delete=models.CASCADE, null=True)
    comment_writer = models.CharField(max_length=20)
    comment_content = models.TextField(null=True)
    # comment_board_kind = models.CharField(max_length=20)

    def __str__(self):
        return self.title


# 게시물 별 이미지 db
class Image(models.Model):
    content = models.ForeignKey(BoardAllContentList, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
