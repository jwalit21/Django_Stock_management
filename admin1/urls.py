from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
        url('adminlogin/', views.adminlogin),
        url('adminloggedin/', views.adminloggedin),
        url('validatelogin/', views.validatelogin),
        url('adminlogout/', views.adminlogout),
        url('deleteenduser/', views.deleteenduser),
        url('managefeedback/', views.managefeedback),
        url('answerfeedback/', views.answerfeedback),
        url('adminmanageuser/', views.adminmanageuser.as_view()),
]