from django.urls import path
from . import views

urlpatterns = [
    path('check_string',views.check_string,name='check_string'),
   
]
