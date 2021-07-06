from django.db import models

# Create your models here.
# pk = user_phone
class Member(models.Model):
    user_name = models.CharField(max_length=15,
                                verbose_name="사용자이름")
    user_pw = models.CharField(max_length=15,
                                verbose_name="비밀번호")
    user_phone = models.CharField(max_length=15, 
                                verbose_name="휴대폰번호",
                                primary_key=True)
    c_date = models.DateTimeField() # 날짜 - 자동으로 넣어줄것이다.
    
    def __str__(self):
        return self.user_phone

    # 별도로 테이블명을 지정하고 싶을 때
    class Meta:
        db_table = 'member_member' # SQLite에 보이는 테이블이름


### 추가된부분 ### 
# 프로필 추가
class Profile(models.Model):
    user_name = models.OneToOneField(Member, on_delete=models.CASCADE)
    # User - Profile을 1:1로 연결
    description = models.TextField(blank=True)
    nickname = models.CharField(max_length=40, blank=True)
    image = models.ImageField(blank=True) #,upload_to="profile/%Y/%m" 
    # imagefield 이용하려면 pip install pillow 패키지 설치
    # blank=True 값 채워넣지 않아도 되는 속성