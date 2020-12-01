
from django.urls import path
from . import views
from .views import GreetingView


urlpatterns = [
    path('', views.GreetingView.as_view(), name= "greeting view"),
    path('greetingcard', views.greetingcard, name= "greeting card")
]
