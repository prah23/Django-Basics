from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User,auth

# Create your views here.
def home(request):
    if request.method=="POST":
        user_dict = {
            'username':request.POST.get('username'),
            'password':request.POST.get('password')
        }
        us = auth.authenticate(**user_dict)
        print(us)
        if us is not None:
            auth.login(request,us)
            print('success')
            return render(request,'success.html')
        redirect('reg/')
    else:
        return render(request,'main.html',{'page_details':'Login'})



def regis(request):
    if request.method=="POST":
        user_dict = {
            'username':request.POST.get('username')
        }
        us = User.objects.create(**user_dict)
        us.set_password(request.POST.get('password'))
        us.save()
        print('DONE')
        redirect('/')
    else:
        return render(request,'main.html',{'page_details':'Register'})



def suc(request):
    return render(request,'success.html')