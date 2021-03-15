from django.shortcuts import render, redirect
from user.forms import Userregistrationform,Profileimageform, Userupdateform,\
    Forgotpwdform
from Posts.models import Createpost
from django.contrib.auth.models import User
from django.views.generic import  ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    
    context={'post':Createpost.objects.all()
             }
    return render(request,'home.html',context)

class Postlistview(LoginRequiredMixin,ListView):
    model=Createpost 
    template_name='home.html'
    context_object_name = 'post'
    ordering=['-date_posted']

def register(request):
    if request.method == 'POST':
        form=Userregistrationform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user:login')
    else:
        form=Userregistrationform()
    return render(request,'registration.html',{'context':form})

@login_required
def profile(request):
    user = request.user
    author = Createpost.author
    context = {
                'post':Createpost.objects.filter(author=user)
        }
    return render(request,'profile.html',context)
    
@login_required
def profileupdate(request):# function to update user profile 
    if request.method == 'POST':
        u_form = Userupdateform(request.POST, instance=request.user)
        p_form = Profileimageform(request.POST, request.FILES, instance=request.user.profileimage)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('user:profile')
    else:
        u_form = Userupdateform(instance=request.user)
        p_form = Profileimageform(instance= request.user.profileimage)
        
    context= {         
    'u_form':u_form,
    'p_form':p_form
            
    }
    return render(request,'Update_profile.html',context)