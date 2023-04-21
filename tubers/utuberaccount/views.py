from django.shortcuts import render
from .models import utuberacc
from django.shortcuts import get_object_or_404
# Create your views here.
def utuber(request):
    youtube=utuberacc.objects.all()
    data={
        'youtube':youtube
    }
    return render(request,'utubers/utubers.html',data)
def youtubersdetail(request,id):
    youtube=get_object_or_404(utuberacc,pk=id)
    data={
        'youtube':youtube
    }
    return render(request,'utubers/youtubersdetail.html',data)
def search(request):
    youtube=utuberacc.objects.order_by('created_date')
    cities=set()
    camera=set()
    crews=set()
    for i in utuberacc.objects.raw("select id ,city,cameratype,crew from   utuberaccount_utuberacc "):
        cities.add(i.city)
        camera.add(i.cameratype)
        crews.add(i.crew)
    
    if 'keyword' in request.GET:
       keyword=request.GET['keyword']
       if keyword:
           youtube=youtube.filter(description__icontains=keyword)
    if 'city' in request.GET:
       city=request.GET['city']
       if city:
           youtube=youtube.filter(city__iexact=city)
    if 'cameratype' in request.GET:
       cameratype=request.GET['cameratype']
       if cameratype:
           youtube=youtube.filter(cameratype__icontains=cameratype)
    if 'crew' in request.GET:
       crew=request.GET['crew']
       if crew:
           youtube=youtube.filter(crew__icontains=crew)       
    
    data={
        'youtube':youtube,
        'city':cities,
        'cameratype':camera,
        'crew':crews
    }
    return render(request,'utubers/search.html',data)