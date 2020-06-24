from django.urls import path
from . import views

urlpatterns = [
    path("", views.contact, name="contact"),
    path("need-help", views.need_help, name="need-help")
]
