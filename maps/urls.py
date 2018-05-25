from django.urls import path,include
from .import views
urlpatterns = [
    path('',views.index),
    path('buildings/<str:building>/',views.buildings),
    path('location/체육관/',views.gym),
    path('location/도서관/',views.library),
    path('location/3층 복도/',views.hall),
    path('location/3층 엘레베이터 앞/',views.elevator),
    path('location/인터넷 룸/',views.internet_room),
    path('location/분임 토의실/',views.debate_room),
    path('location/도서관 입구/',views.lib_entrance),
    path('location/도서관 내부/',views.lib_inside),


]
