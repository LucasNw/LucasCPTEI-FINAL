from django.contrib.admindocs.views import ViewIndexView
from django.urls import path
from .views import index


urlpatterns = [
    path('', ViewIndexView.as_view(), name='index'),
]