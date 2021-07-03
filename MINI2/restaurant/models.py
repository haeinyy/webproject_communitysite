from django.db import models

# Create your models here.
class Rest(models.Model):
    rest_update = models.DateTimeField() #등록 날짜
    rest_name = models.CharField(max_length=100) # 가게명
    rest_score = models.FloatField(default=0) # 평점
    rest_address = models.TextField(default='') # 주소
    rest_kind = models.CharField(max_length=100, default='') # 음식종류
    rest_seenum = models.IntegerField() #조회수
    # est_url = models.CharField(max_length=100) #망고플레이트 주소
    rest_rmd = models.CharField(max_length=100, default='') #추천명 : 공무원(offi)/연구원(kfq)
    
class Review(models.Model):
    review_user = models.CharField(max_length=100) #user 전화번호 등 id
    review_score = models.FloatField() #리뷰점수
    review_content = models.TextField() #리뷰내용
    rest = models.ForeignKey(Rest, on_delete=models.CASCADE) #포린키

class Like(models.Model):
    like_user = models.CharField(max_length=100) #좋아요 누른 전화번호
    like = models.ForeignKey(Rest, on_delete=models.CASCADE) #포린키
