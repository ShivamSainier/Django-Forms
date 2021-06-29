from django.shortcuts import render,HttpResponse,redirect
from .forms import Bookform,userform
from .models import Book
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
@login_required(login_url='main')
def home(request):
    obj=Book.objects.all()
    if request.method=="POST":
        search=request.POST['search_book']
        search_book=Book.objects.filter(name__contains=search)
        context={'obj':search_book}
        return render(request,'home.html',context)
    context={'obj':obj}
    return render(request,'home.html',context)




@login_required(login_url='main')
def addbook(request):
    form=Bookform()
    if request.method=="POST":
        form=Bookform(request.POST ,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            messages.info(request,"invalid Information")
            return redirect('addbook')
    else:
    
        return render(request,'addbook.html',{'form':form})

def deshboard(request):
    return render(request,"dashboard.html")

@login_required(login_url='login_admin')
def admindeshboard(request):
    books=Book.objects.all()
    if request.method=="POST":
        search=request.POST['search_book']
        search_book=Book.objects.filter(name__contains=search)
        context={'books':search_book}
        return render(request,'admindeshboard.html',context)
    else:
        context={'books':books}
        return render(request,"admindeshboard.html",context)

def adminusers(request):
    users=User.objects.all()
    context={
        'users':users
    }
    return render(request,"adminusers.html",context)

def delete_book(request,id):
    book=Book.objects.get(id=id)
    book.delete()
    return redirect('admindeshboard')

def update_book(request,id):
    form=Bookform()
    model=Book.objects.get(id=id)
    if request.method=="POST":
        form=Bookform(request.POST,request.FILES,instance=model)
        if form.is_valid():
            form.save()
            return redirect('admindeshboard')


    return render(request,'addbook.html',{'form':form})

def logout(request):
    auth.logout(request)
    return redirect('home')

def main(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request,"invalid user")
            return redirect('main')
    else:
        return render(request,"main.html")

def login_admin(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            if user.is_staff==True:
                auth.login(request,user)
                return redirect('deshboard')
            else:
                messages.info(request,"Student id is not allowed")
                return redirect('login_admin')
        else:
            messages.info(request,"invalid Admin login")
            return redirect('login_admin')
    else:
       return render(request,"login_admin.html")
    
def adduser(request):
    if request.method=="POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        if((first_name and last_name and email and username and password)==''):
            messages.info(request,'Invalid User')
        else:
            user=User.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username,password=password)
            user.save()
            return redirect('addusers')
    else:
        return render(request,"adduser.html")

def delete_user(request,id):
    model=User.objects.get(id=id)
    model.delete()
    return redirect('adminusers')

def update_user(request,id):
    if request.method=="POST":
        model=User.objects.get(id=id)
        form=userform(request.POST ,instance=model)
        if form.is_valid():
            form.save()
            return redirect('adminusers')
    else:
        form=userform()
        return render(request,"adduser.html",{'form':form})