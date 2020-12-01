from django.shortcuts import render
from django.views import View
from .models import GreetingCard
from django.http import HttpResponse, JsonResponse
from django.core import serializers
import json

# Create your views here.
class GreetingView(View):
    def get(self, request):
        greeting_qs = GreetingCard.objects.all()
        #data = serializers.serialize("json", greeting_qs)
        print(type(greeting_qs))
        self.greeting_ql = list(greeting_qs.values('name', 'message'))
        return JsonResponse(self.greeting_ql, safe= False)

def greetingcard(request):
    greeting_qs = GreetingCard.objects.all()
    greeting_ql = list(greeting_qs.values('name', 'message'))
    return render(request, 'greetingcard.html', {'greeting_ql' : greeting_ql})

