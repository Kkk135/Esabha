from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def indexview(request):
    return render(request,'index.html')
@login_required
def dashboardview(request):
    return render(request,'dashboard.html')

# def login(request):
#     return render(request,'login.html')

def registerview(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form = UserCreationForm()
    return render(request,'registration/register.html',{'form':form})

# def logout(request):
#     return render(request,'logout.html')
