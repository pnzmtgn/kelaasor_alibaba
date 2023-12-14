from django.http.response import HttpResponse, JsonResponse

def list(request):

    flights = {
        "flight_name": "Iran Air" ,
        "fight_number": "8939020R",
        "sit_number": "23" ,
        "price": "1200$" 
    }
    
    return JsonResponse(flights)

# def list(request):

#     flights = {
#         "flight_name": "Iran Air" ,
#         "fight_number": "8939020R",
#         "sit_number": "23" ,
#         "price": "1200$" 
#     }
    
#     return JsonResponse(flights)