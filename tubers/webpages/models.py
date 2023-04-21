from django.db import models

# Create your models here.
class team(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    role=models.CharField(max_length=100)
    fblink=models.CharField(max_length=100)
    instalink=models.CharField(max_length=100)
    photo=models.ImageField(upload_to='media/team/%Y/%m/%d/')
    utubelink=models.CharField(max_length=250,default='https://www.youtube.com/')
    created_date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.firstname
class slider(models.Model):
    headline=models.CharField(max_length=255)
    subtitle=models.CharField(max_length=255)
    button_text=models.CharField(max_length=255)
    photo=models.ImageField(upload_to='media/slider/%Y/',null=True)
    created_date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.headline