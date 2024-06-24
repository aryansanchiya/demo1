from django.urls import path
from . import views

urlpatterns = [
    path('insert/', views.insert_data, name='insert_data'),
    path('get/', views.get_data, name='get_data'),
]
