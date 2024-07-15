from django.http import HttpResponse

def home_pg(request):
    return HttpResponse("This is home page")