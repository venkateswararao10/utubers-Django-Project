from django.shortcuts import render,HttpResponse,redirect
from .models import slider,team
from utuberaccount.models import utuberacc
# Create your views here.
def home(request):
    sli=slider.objects.all()
    t=team.objects.all()
    utuberac=utuberacc.objects.order_by('created_date').filter(isfeatured=True)
    allutuber=utuberacc.objects.order_by('created_date')
    data={
        'sliders':sli,
        'teams':t,
        'youtuber':utuberac,
        'allutuber':allutuber
    }
    return render(request,'webpages/home.html',data)
def about(request):
    return render(request,'webpages/about.html')
def services(request):
    return render(request,'webpages/services.html')
def contact(request):
    return render(request,'webpages/contact.html')