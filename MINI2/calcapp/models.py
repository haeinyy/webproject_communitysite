from django.db import models
from member.models import Member
from django.utils import timezone

class Attendences(models.Model):
    # name = models.ForeignKey(Member, on_delete=models.DO_NOTHING) # cascade 종류 어떻게 해야할지
    user_phone = models.ForeignKey(Member, on_delete=models.DO_NOTHING) 
    name = models.CharField(max_length=50)
    attend = models.IntegerField(default=0)
    absent = models.IntegerField(default=0)
    time =  models.FloatField()
    time_rate =  models.FloatField()
    day_rate = models.FloatField()
    time_cum_rate = models.FloatField()
    day_cum_rate = models.FloatField()  

    def __str__(self):
        return f'{self.name}-{self.user_phone}'

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    # python -m pip install Pillow 설치 필요
    images = models.ImageField(blank=True, upload_to="notice_img", null=True)

    # 해인추가
    user = models.CharField(max_length=20) # main user db랑 연결 해야함
    board_kind = models.CharField(max_length=20)



    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:100]



# class Notices(models.Model):
#     object = models.Manager()
#     n_title = models.CharField(max_length=100)
#     n_body = models.TextField()
#     n_hit = models.PositiveBigIntegerField(default=0)
#     n_input_data = models.DateTimeField('data published', default=timezone.now)

#     def __str__(self):
#         return self.n_title

#     @property
#     def update_counter(self):
#         self.n_hit = self.n_hit + 1
#         self.save()