from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.contrib import auth

def sayhello (request):
	return HttpResponse("Hello Django")

def bossPage(request,username):
	now = datetime.now()
	return render (request , "bossPage.html" , locals() )
	
def IEsPage(request,username):
	now = datetime.now()
	return render (request , "IEsPage.html" , locals() )

def foremanPage(request,username):
	now = datetime.now()
	return render (request , "foremanPage.html" , locals() )

def operPage(request,username):
	now = datetime.now()
	return render (request , "operPage.html" , locals() )

def loginPage(request):
	return render (request,"login.html")

def login(request):

    if request.user.is_authenticated(): 
        return HttpResponseRedirect('/index/')

    account = request.POST.get('account', '')
    password = request.POST.get('password', '')
    
    user = auth.authenticate(account=account, password=password)

    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect('/index/')
    else:
        return render_to_response('login.html') 
# Create your views here.
