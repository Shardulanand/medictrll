from django.shortcuts import render,redirect
from app1.forms import *
from django.core.mail import send_mail


app_name="app1"


def base(request):
    return render(request,'base.html')

def base2(request):
    return render(request,'base2.html')
def index(request):
    return render(request,'app1/index.html')
def callback(request):
    if request.method =="POST":
        form=message_Form(request.POST)
        if form.is_valid():
            form.save()
            send_mail(
                'New Message',
                'New Message from Site',
                'contactmedictrl@gmail.com',
                ['shardulanand1@gmail.com'] ,
                fail_silently=False,
            )
        else:
            print(form.errors)
            return redirect('app1:indexurls')
    form=message_Form()
    context={
        'form':form,
    }
    return render(request,'app1/callback.html',context)
def about(request):
    return render(request,'app1/aboutus.html')
def policy(request):
    return render(request,'app1/privacy.html')