from django.db import models

# Create your models here.

#  모든 게신판 게시물 db
class BoardAllContentList(models.Model):
    title = models.CharField(max_length=100)
    # user_id = models.ForeignKey(, on_delete=models.CASCADE) # main user db랑 연결 해야함
    date = models.DateTimeField()
    seenum = models.IntegerField()
    like = models.IntegerField()
    board_kind = models.CharField(max_length=20)

# 모든 게시판 댓글 db
# class Board_comment(models.Model):
#     comment_content = models.ForeignKey(re)
