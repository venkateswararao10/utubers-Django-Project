from django.urls import path
from . import views
urlpatterns = [
    path('',views.utuber,name='utuber'),
    path('<int:id>',views.youtubersdetail,name='youtubersdetail'),
    path('search',views.search,name='search')
]