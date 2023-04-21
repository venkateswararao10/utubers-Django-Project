from django.db import models

# Create your models here.
from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
# Create your models here.
class utuberacc(models.Model):
    crewchoice=(('solo','solo'),('small','small'),('large','large'))
    camerachoice=(('canon','canon'),('nikon','nikon'),('sony','sony'))
    categorychoice=(('entertainment','entertainment'),('technology','technology'),('lifestyle','lifestyle'),('education','education'),('vlogs','vlogs'),('others','others'))
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    photo=models.ImageField(upload_to='media/utuber/%Y/%m/')
    video_url=models.CharField(max_length=100)
    description=RichTextField()
    city=models.CharField(max_length=100)
    age=models.IntegerField()
    crew=models.CharField(choices=crewchoice,max_length=100)
    cameratype=models.CharField(choices=camerachoice,max_length=100)
    subscribercount=models.IntegerField()
    category=models.CharField(choices=categorychoice,max_length=100)
    isfeatured=models.BooleanField(default=False)
    created_date=models.DateTimeField(default=datetime.now,blank=True)
    def __str__(self):
        return self.name