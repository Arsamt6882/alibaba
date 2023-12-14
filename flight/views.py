from django.http.response import HttpResponse, JsonResponse
def list(request):
    flight={
        "name":"ar",
        "no":"222234",
        "capacity":"pro",
        "price":"550"
    } 
    return JsonResponse(flight)




