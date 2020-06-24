from django.urls import path
from . import views

urlpatterns = [
    path('all', views.buses, name='buses'),
    path('<int:id>/details', views.details, name='details')
]
