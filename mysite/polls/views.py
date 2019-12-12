from django.shortcuts import HttpResponse

def index(request):
    return HttpResponse("Olá Mundo! Você está em Polls index")