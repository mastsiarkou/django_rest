from django.urls import path
from . import views

urlpatterns = [
    path('api/event/', views.TimerList.as_view()),
]