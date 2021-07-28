from django.urls import path
from bookmananger.views import index

urlpatterns = [
    path('index/', index)
]