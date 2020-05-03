from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.models import User
from dashboard1 import views as v
from django.contrib.auth.decorators import login_required
from dashboard1.models import stock
from django.core.mail import send_mail
from django.db.models import F
import string
import random

# Create your views here.
def forgotpassword(request):
    return render(request,'forgotpasswordhome.html',context=None)

def forgotpasswordsuccessfull(request):
    username=request.POST.get('username','')
    email=request.POST.get('email','')
    password=request.POST.get('password','')
    user_obj=User.objects.get(username__exact=username)
    user_obj.set_password(password)
    user_obj.save()
    del request.session['token']
    del request.session['username']
    del request.session['email']
    return render(request,'login.html',{'msg':'password reset successfully'})


def forgotpassworduserverification(request):
    username=request.POST.get('username','')
    obj=User.objects.filter()
    list_username=[]
    for i in obj:
        list_username.append(i.username)
    value=False
    for i in list_username:
        if(username==i):
            value=True
    if value:
        user_obj=User.objects.get(username=username)
    else:
        return render(request,'login.html',{'msg':'Email address entered by you is wrong or you are not a user yet !!!'})
    if value :
        email=user_obj.email
        letters = string.ascii_lowercase
        token=""
        token_validation=token.join(random.choice(letters) for i in range(50))
        token=""
        request.session['token']=token_validation
        request.session['username']=username
        request.session['email']=email
        print(token_validation)
        msg='Please go to this url for setting up new password http://127.0.0.1:8000/logintestapp/forgotpasswordmain?username='+username+'&email='+email+'&token='+token_validation
        send_mail(
            'automated forgot password',
            msg,
            'jwalitshah2q@gmail.com',
            [email],
            fail_silently=False
        )
        return render(request,'login.html',{'msg':'Email sent to your registered Email address. Read Email carefully and go to the page given in email. And valid threw only for one attempt.'})
    
    else:
        return render(request,'login.html',{'msg':'Email address entered by you is wrong or you are not a user yet !!!'})


def forgotpasswordmain(request):
    username=request.GET.get('username','')
    email=request.GET.get('email','')
    token=request.GET.get('token','')
    token_validation = request.session.get('token')
    username_validation = request.session.get('username')
    email_validation = request.session.get('email')
    if( (token_validation == token) & (username_validation == username) & (email_validation == email) ):
        return render(request,'forgotpasswordmain.html',{'username':username,'email':email})
    else:
        if( request.session.get('token') ):
            del request.session['token']
        if( request.session.get('username') ):
            del request.session['username']
        if( request.session.get('email') ):
            del request.session['email']
        return render(request,'login.html',{'msg':'Invalid Url for Forgot password !!!!'})


def login(request):
    return render(request,'login.html',context=None)


def auth_view(request): 
    username = request.POST.get('username', '') 
    password = request.POST.get('password', '') 
    user = auth.authenticate(username=username, password=password) 
    if user is not None: 
        auth.login(request, user) 
        return HttpResponseRedirect('/logintestapp/loggedin/') 
        
    else: 
        return HttpResponseRedirect('/logintestapp/invalidlogin/')


@login_required(login_url='/logintestapp/login/')
def loggedin(request):
    stock_empty_object=stock.objects.filter(stock_quantity__lte=F('stock_empty')).filter(stock_username=request.user.username)
    return render(request,'loggedin.html', {"full_name": request.user.username,"stock_empty_object": stock_empty_object})


def invalidlogin(request):
    return render(request,'login.html',{'msg':'Invalid Credentials,please login again.'})


def logout(request):
    auth.logout(request)
    return render(request,'login.html',{'msg':'You logged out successfully'})


def addCustomer(request):
    userName = request.POST.get('username', None)
    userPass = request.POST.get('password', None)
    userMail = request.POST.get('email', None)
    user = User.objects.create_user(username=userName,
                                 email=userMail,
                                 password=userPass)
    return render(request,'login.html',{'msg':'You registered successfully !! please login here'})



def newCustomer(request):
    return render (request,'register.html')
