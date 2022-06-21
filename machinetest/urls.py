
from django.contrib import admin
from django.urls import path,include
from testapp.views import check_string

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',check_string,name='check_string'),
]
