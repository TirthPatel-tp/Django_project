from django.contrib import admin
from django.urls import path, include
from . import views
from .views import activate

urlpatterns = [
    path('',views.home,name="home"),
    path('signup', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
    path('signout', views.signout, name="signout"),
    path('activate/<uidb64>/<token>/', activate, name="activate"),
    path('Badmintion', views.Badmintion , name="Badmintion"),
    path('Index', views.Index , name="Index"),
    path('download-cv/', views.download_cv, name='download_cv'),
]