# here we are import path from in-built django-urls
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


# here we are importing all the Views from the views.py file
from . import views

urlpatterns = [
    path('', views.index, name='weather'),
]
