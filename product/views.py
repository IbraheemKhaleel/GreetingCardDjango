from django.shortcuts import render
from django.views import View
from .models import GreetingCard
from django.http import HttpResponse, JsonResponse
from django.core import serializers
import json

# Create your views here.
def greetingcard(request):
    """
    Created method to go to greeting card page which helps ajax to get data from home page.
    return: greeting card html page
    """
    return render(request, 'greetingcard.html')

class GreetingView(View):
    """
    Created class to get view of greeting card objects
    return: dictionary of database elements stored
    """        
    def get(self, request):
        try:
            greeting_qs = GreetingCard.objects.all()
            greeting_ql = list(greeting_qs.values('name', 'message'))
            return HttpResponse(json.dumps(greeting_ql))
        except Exception:
            return HttpResponse("Field not found in database")
