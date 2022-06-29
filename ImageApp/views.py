from django.shortcuts import render,redirect
from ImageApp.models import UserProfile
import os
# Create your views here.
def load(request):
    return render(request,'add_user.html')

def add_user(request):
    if request.method=="POST":
        name=request.POST.get('username')
        email=request.POST.get('email')
        number=request.POST.get('number')
        image=request.FILES.get('file')
        user=UserProfile(UserName=name,Email=email,ContactNumber=number,Image=image)
        user.save()
        return redirect('show')

def show(request):
    user=UserProfile.objects.all()
    return render(request,'show_user.html',{'users':user})

def edit(request,pk):
    user=UserProfile.objects.get(id=pk)
    if request.method=="POST":
        if len(request.FILES)!=0:
            if len(user.Image)>0:
                os.remove(user.Image.path)
            user.Image=request.FILES.get('file')
        user.UserName=request.POST.get('username')
        user.Email=request.POST.get('email')
        user.Number=request.POST.get('number')
            
        user.save()
        return redirect('show')
    return render(request,'edit.html',{'users':user})

# def delete(request,pk):
#     user=UserProfile.objects.get(id=pk)
#     user.delete()
#     return redirect('show')
    
def delete(request,pk):
    user=UserProfile.objects.get(id=pk)
    if user.Image:
        user.Image.delete()
    user.delete()
    return redirect("show")        