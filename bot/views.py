from django.shortcuts import render
from django.http import HttpResponse

def chatbot(request):
    return render(request, 'chatbot.html')
