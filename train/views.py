from django.http.response import HttpResponse, JsonResponse
from .models import Train, Station


def list(request):

trains = Train.objects.all()
trains_list = []
for item in trains:
    dictionary = {
        "name": item.name,
        "origin" : item.origin.name,
        "destination" : item.destination.name,
        "price" : item.price
    }
    trains_list.append(dictionary)
return HttpResponse(trains_list)


def list2(request):

   Station = Station.objects.all()
airport_list = []
for item in Station:
    dictionary = {
        "name": item.name,
        "No" : item.No,
        "city" : item.city,
    }

    station_list.append(dictionary)
return HttpResponse(airport_list)  