from django.db import models
from member.models import Member

class AttendHistroy(models.Model):

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
        return f'{self.name}-{self.time}'