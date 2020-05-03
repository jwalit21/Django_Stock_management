from django.shortcuts import redirect, render
from django.views.generic import TemplateView  
from django.http import HttpResponseRedirect  
from django.views import generic
from dashboard1.models import stock
from django.contrib.auth.models import User
from dashboard1.models import feedback
from django.contrib.auth.decorators import login_required
from django.template.context_processors import csrf
from django.db.models import F
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def adminlogin(request):
    return render(request,'adminlogin.html',context=None)

@login_required(login_url='/admin1/adminlogin/')
def adminloggedin(request):
    return render(request,'adminloggedin.html',context=None)

def adminlogout(request):
    return render(request,'adminlogin.html',{'msg':'Logged out succssfully !!! '})

def validatelogin(request):
    username=request.POST.get('username')
    password=request.POST.get('password')
    if(username=="jwalit" and password=="123"):
        total_user=User.objects.count()
        request.session['total_user']=total_user
        total_stock=stock.objects.count()
        request.session['total_stock']=total_stock
        total_feedback=feedback.objects.count()
        request.session['total_feedback']=total_feedback
        print(total_feedback)
        print(total_stock)
        print(total_user)
        return render(request,'adminloggedin.html',{'total_user':total_user,'total_feedback':total_feedback,'total_stock':total_stock})
    else:
        return render(request,'adminlogin.html',{'msg':'Invalid credentials Admin !!!!'})


class adminmanageuser(generic.ListView):
    model = User

def deleteenduser(request):
    user_username=request.GET.get('user_username')
    user_obj=User.objects.filter(username=user_username).delete()
    return render(request,'adminloggedin.html',{'msg':'End user deleted successfully !!!!'})
    
def managefeedback(request):
    feedback_obj=feedback.objects.filter()
    print(feedback_obj)
    return render(request,'adminfeedback.html',{'feedback_obj':feedback_obj})   

def answerfeedback(request):
    feedback_id=request.GET.get('feedback_id')
    feedback_msg=request.GET.get('feedback_msg')
    username=request.GET.get('username')
    feedback_que=request.GET.get('feedback_que')
    print(feedback_msg,feedback_id,feedback_que,username)
    feedback_obj1=feedback.objects.filter(feedback_id=feedback_id).update(username=username,feedback_id=feedback_id,feedback_que=feedback_que,feedback_msg=feedback_msg)
    feedback_obj=feedback.objects.filter()
    return render(request,'adminfeedback.html',{'feedback_obj':feedback_obj,'msg':'Answer to the Feedback given successfully !!!'})