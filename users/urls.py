from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path("faculty-signup", views.faculty_signup, name="faculty-signup"),
    path("student-signup", views.student_signup, name="student-signup"),
    path("login", views.login, name="login"),
    url(r'activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',
        views.activate, name='activate'),
    path("logout", views.logout, name="logout"),
    path("faculty/profile/edit", views.edit_faculty_profile,
         name="edit-faculty-profile"),
    path("student/profile/edit", views.edit_student_profile,
         name="edit-student-profile"),
    path("bus-pass", views.bus_pass, name="bus-pass"),
    path("pass/<int:id>/print-pass", views.print_pass, name="print-pass"),
    path("pass/<int:id>/delete-pass", views.delete_pass, name="delete-pass"),
    path('charge/', views.charge, name="charge"),
    path('success/<str:args>/', views.successMsg, name="success"),
    path('payment/',views.payment,name='checkout')
]
