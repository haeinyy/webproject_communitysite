from django.db import models

# Create your models here.
# pk = user_phone
class Member(models.Model):
    user_name = models.CharField(max_length=15)
    user_pw = models.CharField(max_length=15)
    user_phone = models.CharField(max_length=15, primary_key=True)
    c_date = models.DateTimeField() # 날짜 - 자동으로 넣어줄것이다.
    