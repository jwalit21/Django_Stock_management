from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class stock(models.Model):
    stock_username=models.CharField(max_length=60,default='')
    stock_name = models.CharField(max_length=100)
    stock_id = models.CharField(max_length=20)
    stock_catagory=models.CharField(max_length=50,default='')
    stock_prize=models.IntegerField()
    stock_quantity=models.IntegerField()
    stock_empty=models.IntegerField(default=0)

class feedback(models.Model):
    username=models.CharField(max_length=60)
    feedback_id=models.AutoField(primary_key=True)
    feedback_msg=models.CharField(max_length=3000,null=False,default='')
    feedback_que=models.CharField(max_length=3000)