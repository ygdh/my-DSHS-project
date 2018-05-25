from django.shortcuts import render
from django.http import HttpResponse

from .models import Location
# Create your views here.
def index(request):
	locations = Location.objects.all() #Location에 있는 모든 객체를 불러옵니다.
	context = {'locations' : locations} #context에 모든 장소에 대한 정보를 저장
	return render(request,'maps/index.html',context)

def buildings(request, building):
	locations = Location.objects.filter(building = building)
	context = {'locations':locations,
	'building' : building,
	}
	return render(request, 'maps/building.html',context)

def gym(request):
	return render(request,'maps/gym.html')

def library(request):
	return render(request,'maps/library.html')

def hall(request):
	return render(request,'maps/hall.html')

def elevator(request):
	return render(request,'maps/elevator.html')

def internet_room(request):
	return render(request,'maps/internet_room.html')

def debate_room(request):
	return render(request,'maps/debate_room.html')
	
def lib_entrance(request):
	return render(request,'maps/lib_entrance.html')

def lib_inside(request):
	return render(request,'maps/lib_inside.html')