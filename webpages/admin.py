from django.contrib import admin
from webpages.models import slider,team
from django.utils.html import format_html
# Register your models here.
class teamadmin(admin.ModelAdmin):
    def myphoto(self,object):
        return format_html('<img src="{}" width="40"/>'.format(object.photo.url))
    list_display=['id','myphoto','firstname','role','created_date']
    list_display_links=['id','firstname']
    search_fields=['firstname','role']
    list_filter=['role']
    date_hierarchy='created_date'
admin.site.register(slider)
admin.site.register(team,teamadmin)