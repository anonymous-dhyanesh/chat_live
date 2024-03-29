from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path('', views.landing, name="landing"),
    path('<str:room>/', views.room, name="room"),
    path('checkview', views.checkview, name="checkview"),
    path('send', views.send, name="send"),
    path('getMessages/<str:room>/', views.getMessages, name="getMessages"),
    path('home', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('datasaver', views.datasaver, name='datasaver')

]