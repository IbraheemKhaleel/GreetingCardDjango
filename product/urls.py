
from django.urls import path
from . import views
from .views import GreetingView


urlpatterns = [
    path('greetingcard/', views.greetingcard, name= "greeting view"),
    path('', views.GreetingView.as_view())
]
