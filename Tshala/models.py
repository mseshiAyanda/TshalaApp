from django.db import models
from django.contrib.auth.models import User
import psycopg2 as Database
from .validators import file_size

# Create your models here.


class Video(models.Model):
    STATUS = (
			('Pending', 'Pending'),
			('Out for delivery', 'Out for delivery'),
			('Delivered', 'Delivered'),
			)
            
    
    caption=models.CharField(max_length=90)
    video=models.FileField(upload_to="video/%y", blank=True, validators=[file_size])
    date=models.DateTimeField(auto_now_add=True, null=True)



class Add(models.Model):
    videos=models.ForeignKey(Video, null=True, on_delete= models.SET_NULL)
    country=models.CharField(max_length=40)
    city=models.CharField(max_length=50)
    busstype=models.CharField(max_length=50)
    companyname=models.CharField(max_length=40)
    regnumber=models.CharField(max_length=40)
    nameofd=models.TextField(max_length=400)
    nameofs=models.TextField(max_length=440)

    
    