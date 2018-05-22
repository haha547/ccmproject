from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect

#############################
'''
def selectPage(request , position):
	now = datetime.now()
	if position == 'boss':
		return render (request , "bossPage.html" , locals())
	elif position == 'IEs':
		return render (request , "IEsPage.html" , locals())
	elif position == 'foreman':
		return render (request , "foremanPage.html" , locals())
	else:
		return render (request , "operPage.html" , locals())
'''
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

def index(request):
	if request.user.is_authenticated:
	   name=request.user.username
	return render(request, "index.html", locals())

def login(request):
	if request.method == 'POST':
		name = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(username=name, password=password)
		if user is not None:
			if user.is_active:
				auth.login(request,user)
				return redirect('/index/')
				message = '登入成功！'
			else:
				message = '帳號尚未啟用！'
		else:
			message = '登入失敗！'
	return render(request, "login.html", locals())
	
def logout(request):
	auth.logout(request)
	return redirect('/index/')	