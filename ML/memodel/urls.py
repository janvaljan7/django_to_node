from django.urls import path
from memodel import views


urlpatterns = [
    path('', views.getinfo.as_view(), name='model')
]


