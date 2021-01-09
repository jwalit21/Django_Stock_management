from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
                url('/', views.home),
                url('home/', views.home),
                url('addstockinfo/', views.addstockinfo),
                url('deletestockdata/', views.deletestockdata),
                url('updatestockinfo/', views.updatestockinfo),
                url('addstockdata/', views.addstockdata),
                url('updatestockdata/', views.updatestockdata),
                url('searchname/',views.searchname),
                url('searchcat/',views.searchcat),
                url('feedbackinfo/',views.feedbackinfo),
                url('feedbackdata/',views.feedbackdata),
                url('instagram/', views.instagram),
                url('facebook/', views.facebook),
                url('twitter/', views.twitter),
                url('stocks/', views.viewstockdata.as_view()),
            ]