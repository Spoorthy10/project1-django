from django.http import HttpResponse

def sample(request):
    return HttpResponse("hello python")