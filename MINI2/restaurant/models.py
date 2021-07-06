from django.db import models

# Create your models here.
class Rest(models.Model):
    rest_name = models.CharField(max_length=100) # 가게명
    rest_score = models.FloatField(default=0) # 평점
    rest_address = models.TextField(default='') # 주소
    rest_kind = models.CharField(max_length=100, default='') # 음식종류
    rest_seenum = models.IntegerField(default=1) #조회수
    rest_img1 = models.CharField(max_length=200) #망고플레이트 첫번째 사진 주소
    rest_img2 = models.CharField(max_length=200) #망고플레이트 두번째 사진 주소
    rest_url = models.URLField() #망고플레이트 가게주소
    rest_rmd = models.CharField(max_length=100, default='user') #추천명 : 공무원(offi)/연구원(kfq)
    rest_update = models.DateTimeField() #등록 날짜
    rest_tel = models.CharField(max_length=15, default=None)
    rest_price = models.CharField(max_length=100, default=None)
    rest_starscore = models.CharField(max_length=10, default=None)

class Review(models.Model):
    review_score = models.FloatField() #리뷰점수
    review_content = models.TextField() #리뷰내용
    review_writer = models.CharField(max_length=20) 
    review_date = models.DateTimeField(auto_now_add=True)
    rest_id = models.ForeignKey(Rest, on_delete=models.CASCADE) #포린키

    def __str__(self):
        return self.rest_name

class Rest_Like(models.Model):
    like_user = models.CharField(max_length=100) #좋아요 누른 전화번호
    like_rest = models.ForeignKey(Rest, on_delete=models.CASCADE) #포린키
    #게시글 포린키

