from django.urls import path
from . import views
urlpatterns = [
    path('loginuser',views.loginuser,name='loginuser'),
    path('register',views.register,name='register'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('logout',views.logoutuser,name='logout')
]