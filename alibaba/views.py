from django.http.response import HttpResponse, JsonResponse

def welcom (request):
    return HttpResponse("welcom is alibab")


def about(request):
    return HttpResponse("here is about page")


def flight(request):
    flight={
        "name":"ar",
        "no":"222234",
        "capacity":"pro",
        "price":"550"
    } 
    return JsonResponse(flight)

  
