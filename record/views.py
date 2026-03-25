from django.shortcuts import render, redirect, get_object_or_404
from .models import Record 
from .forms import  RegisterForm
from django.contrib.auth import login, logout 
from django.contrib.auth.decorators import login_required
def signup_view(request):
    if request.method =='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('record_list')
    else:
        form = RegisterForm()
    return render(request,'signup.html', {'form': form})
@login_required
def record_list(request):
    records = Record.objects.filter(owner=request.user)
    return render(request,'list.html', {'records': records})



def logout_view(request):
    logout(request)
    return redirect('login')
