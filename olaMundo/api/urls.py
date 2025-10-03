from django.urls import path
from api.views import index, apiOla

urlpatterns = [
    path('api/ola/', apiOla),
    path('', index),

]
