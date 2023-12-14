from django.http.response import HttpResponse, JsonResponse

def welcome(request):
    return HttpResponse("Welcome to Alibaba!")

def about(request):
    return HttpResponse("This is about page!")

def contact(request):
    return HttpResponse("This is contact page!")

def flights(request):
    flights = {"flight_name": "Iran Air" ,
                   "fight_number": "8939020R",
                   "sit_number": "23" ,
                   "price": "1200$" }
    return JsonResponse(flights)

def bus(request):
    bus = {
        "Bus_name": "Auto Safar" ,
        "bus_number": "1187520R",
        "sit_number": "23" ,
        "price": "120$"
        }
    return JsonResponse(bus)