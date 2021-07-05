from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE


# Create your models here.

#  모든 게신판 게시물 db
class BoardAllContentList(models.Model):
    title = models.CharField(max_length=100)
    # user_id = models.ForeignKey(, on_delete=models.CASCADE) # main user db랑 연결 해야함
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    seenum = models.IntegerField(null=True)
    like = models.IntegerField(null=True)
    board_kind = models.CharField(max_length=20)

    def __str__(self):
        return self.title


# 게시물 별 이미지 db
class Image(models.Model):
    content = models.ForeignKey(BoardAllContentList, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)


# 모든 게시판 댓글 db
class Board_comment(models.Model):
    content = models.ForeignKey(BoardAllContentList, on_delete=models.CASCADE, null=True, related_name='content')
    comment_date = models.DateTimeField(auto_now_add=True)
    # comment_writer = models.ForeignKey(,on_delete=models.CASCADE, null=True)
    comment_content = models.TextField(null=True)
    # comment_board_kind = models.CharField(max_length=20)

    # class Meta:
    #     orerding  = ['-id']
