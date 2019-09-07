from django.shortcuts import render, redirect
from .forms import userRegister as ucform,userUpdateForm,updateProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
def register(request):
    if request.method == "POST":
        form = ucform(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,'Account created for %s' % username)
            return redirect('login')
    else:
        form=ucform()
    return render(request,'users/register.html',{'form':form})
@login_required
def profile(request):
    if request.method == "POST":
        u_form = userUpdateForm(request.POST,instance=request.user)
        up_form = updateProfileForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and up_form.is_valid():
            up_form.save()
            u_form.save()
            messages.success(request, 'Your Account is Updated')
            return redirect('user_profile')
    else:
        u_form = userUpdateForm(instance=request.user)
        up_form = updateProfileForm(instance=request.user.profile)
    context={
        'u_form':u_form,
        'up_form':up_form

    }
    return render(request,'users/profile.html',context)