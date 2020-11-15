from django.urls import path
from APIAPP import views

urlpatterns = [
    path('add', views.AddData.as_view()),
    path('get', views.SendData.as_view()),
]
