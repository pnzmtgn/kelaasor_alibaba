from django.http.response import HttpResponse, JsonResponse

def list(request):

    bus = {
        "bus_name": "Auto Safar" ,
        "bus_number": "1129020R",
        "sit_number": "25" ,
        "price": "140$" 
    }
    
    return JsonResponse(bus)