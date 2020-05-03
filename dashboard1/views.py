from django.shortcuts import redirect, render
from django.views.generic import TemplateView  
from django.http import HttpResponseRedirect  
from django.views import generic
from dashboard1.models import stock
from dashboard1.models import feedback
from django.contrib.auth.decorators import login_required
from django.template.context_processors import csrf
from django.db.models import F
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
@login_required(login_url='/logintestapp/login/')
def addstockinfo(request):
    c={"full_name": request.user.username}
    c.update(csrf(request))
    return render(request,'addstockinfo.html', c)

@login_required(login_url='/logintestapp/login/')
def addstockdata(request):
    sname = request.POST.get('stockname', '')
    sid = request.POST.get('stockid', '')
    scat= request.POST.get('stockcat','')
    sprize=request.POST.get('stockprize','')
    squantity=request.POST.get('stockquantity','')
    sempty=request.POST.get('stockempty','') 
    susername=request.user.username
    s = stock(stock_username=susername,stock_name = sname,stock_id = sid,stock_catagory=scat,stock_prize = sprize,stock_quantity = squantity,stock_empty=sempty)
    s.save()
    stock_empty_object=stock.objects.filter(stock_quantity__lte=F('stock_empty')).filter(stock_username=request.user.username)
    return render(request,'loggedin.html',{'stock_empty_object':stock_empty_object,"full_name": request.user.username,'msg':'Data entered successfully !!!'})

@login_required(login_url='/logintestapp/login/')
def updatestockinfo(request):
    stockid=request.GET.get('stock_id','')
    stockname=request.GET.get('stock_name','')
    stockcat=request.GET.get('stock_cat','')
    stockempty=request.GET.get('stock_empty','')
    stockprize=request.GET.get('stock_prize','')
    stockquantity=request.GET.get('stock_quantity','')
    return render(request,'updatestockinfo.html', {"full_name": request.user.username,'stock_id':stockid,'stock_name':stockname,'stock_cat':stockcat,'stock_prize':stockprize,'stock_quantity':stockquantity,'stock_empty':stockempty})

@login_required(login_url='/logintestapp/login/')
def updatestockdata(request):
    sname = request.GET.get('stockname', '')
    sid=request.GET.get('stockid','')
    sprize=request.GET.get('stockprize','')
    sempty=request.GET.get('stockempty','')
    scat= request.GET.get('stockcat','')
    squantity=request.GET.get('stockquantity','')
    susername=request.user.username
    stock_obj=stock.objects.filter(stock_id=sid).update(stock_username=susername,stock_name=sname,stock_catagory=scat,stock_prize=sprize,stock_quantity=squantity,stock_empty=sempty)
    stock_empty_object=stock.objects.filter(stock_quantity__lte=F('stock_empty')).filter(stock_username=request.user.username)
    return render(request,'loggedin.html',{'stock_empty_object':stock_empty_object,"full_name": request.user.username,'msg':'Data updated successfully !!!'})

@login_required(login_url='/logintestapp/login/')
def searchname(request):
    name=request.GET.get('searchname','')
    stock_object=stock.objects.filter(stock_name=name).filter(stock_username=request.user.username)
    stock_empty_object=stock.objects.filter(stock_quantity__lte=F('stock_empty')).filter(stock_username=request.user.username)
    return render(request,'searchname.html',{'stock_object':stock_object,'stock_empty_object':stock_empty_object,"full_name": request.user.username})

@login_required(login_url='/logintestapp/login/')
def searchcat(request):
    cat=request.GET.get('searchcat','')
    stock_object=stock.objects.filter(stock_catagory=cat).filter(stock_username=request.user.username)
    stock_empty_object=stock.objects.filter(stock_quantity__lte=F('stock_empty')).filter(stock_username=request.user.username)
    return render(request,'searchcat.html',{'stock_object':stock_object,'stock_empty_object':stock_empty_object,"full_name": request.user.username})
    
@login_required(login_url='/logintestapp/login/')
def deletestockdata(request):
    stockid=request.GET.get('stock_id','')
    stock_list=stock.objects.filter(stock_id=stockid).filter(stock_username=request.user.username).delete()
    stock_empty_object=stock.objects.filter(stock_quantity__lte=F('stock_empty')).filter(stock_username=request.user.username)
    return render(request,'loggedin.html',{'stock_empty_object':stock_empty_object,"full_name": request.user.username,'msg':'Data deleted successfully !!!'})

@login_required(login_url='/logintestapp/login/')
def feedbackinfo(request):
    full_name=request.user.username
    #fu=feedback.objects.filter(username=full_name)
    feedback_obj=feedback.objects.filter(username=full_name)
    return render(request,'feedback.html',{"full_name": request.user.username,"feedback_obj":feedback_obj})

@login_required(login_url='/logintestapp/login/')
def feedbackdata(request):
    feedback_que=request.GET.get('feedback_que','')
    full_name=request.user.username
    f=feedback(username=full_name,feedback_que=feedback_que)
    f.save()
    stock_empty_object=stock.objects.filter(stock_quantity__lte=F('stock_empty')).filter(stock_username=request.user.username)
    return render(request,'loggedin.html',{"full_name": request.user.username,'stock_empty_object':stock_empty_object,'msg':'Feedback given successfully !!!'})

class viewstockdata(LoginRequiredMixin,generic.ListView):
    login_url = '/logintestapp/login/'
    redirect_field_name = 'redirect_to'
    model = stock

#@login_required(login_url='/logintestapp/login/')
def home(request):
    return render(request,'homepage.html',content_type=None)

@login_required(login_url='/logintestapp/login/')
def facebook(request):
    return redirect("https://facebook.com/")

@login_required(login_url='/logintestapp/login/')
def instagram(request):
    return redirect("https://instagram.com/")

@login_required(login_url='/logintestapp/login/')
def twitter(request):
    return redirect("https://twitter.com/")    