
from django.contrib import admin
from django.utils.html import format_html
from .models import utuberacc
# Register your models here.
class ytadmin(admin.ModelAdmin):
    def myphoto(self,object):
        return format_html('<img src={} width="40"/>'.format(object.photo.url))
    list_display=['id','name','myphoto','subscribercount','isfeatured']
    list_display_links=['name','myphoto']
    list_editable=['isfeatured']
    list_filter=['city','cameratype']
    search_fields=['name']
    
admin.site.register(utuberacc,ytadmin)
