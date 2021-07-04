from django.db import models

# Create your models here.
class Rest(models.Model):
    Rest_name = models.CharField(max_length=100)
    Rest_score = models.FloatField(default=0)
    Rest_address = models.TextField(default='')
    Rest_Tel = models.CharField(max_length=100, default='')
    Rest_kind = models.CharField(max_length=100, default='')
    Rest_price = models.CharField(max_length=100, default='')
    Rest_url = models.CharField(max_length=100)