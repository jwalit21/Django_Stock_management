from django.urls import path
from . import views

urlpatterns=[
    path('login/',views.login),
    path('auth/',views.auth_view),
    path('loggedin/',views.loggedin),
    path('logout/',views.logout),
    path('invalidlogin/',views.invalidlogin),
    path('addCustomer/',views.newCustomer),
    path('createUser/',views.addCustomer),
    path('forgotpassword/',views.forgotpassword),
    path('forgotpasswordsuccessfull/',views.forgotpasswordsuccessfull),
    path('forgotpasswordmain/',views.forgotpasswordmain),
    path('forgotpassworduserverification/',views.forgotpassworduserverification)
]