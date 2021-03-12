from django.shortcuts import render, HttpResponse, redirect
from .models import Video, Add
from django.contrib.auth.models import User, auth

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import *
from django.contrib.auth.forms import UserCreationForm

from .forms import CreateUserForm, Adding_form

from .filters import VedeoFilter
from .forms import Video_form, Adding_form
from .validators import file_size

# Create your views here.login_required
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt

def register(request):
    if request.user.is_authenticated:
        return redirect('Tshala:home')
    else:
            form = CreateUserForm
            if request.method == 'POST':
                form = CreateUserForm(request.POST)
                if form.is_valid():
                    form.save()
                    user = form.cleaned_data.get('username')
                    messages.success(request, 'Account was created for ' + user)

                    return redirect('login')
       
            else:
                return render(request, 'registration/register.html', {'form':form})

def registerbus(request):
    return render(request, 'account/registerbus.html')
    

@csrf_exempt
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('Tshala:home')
    else:

            if request.method == 'POST':
                username = request.POST.get('username')
                password = request.POST.get('password')

                user = authenticate(request, username=username, password=password)

                if user is not None:
                    login(request, user)
                    return redirect('/')
                else:
                    messages.info(request, 'Username or Password is incorrect')
               
     
    return render(request, 'registration/login.html')

def logoutUser(request):
    logout(request)
    return redirect('Tshala:login')
   

@login_required(login_url='Tshala:login')
def home(request):
    video2 = Video.objects.all()
    form2 = Video_form()
    myFilter = VedeoFilter(request.GET, queryset=video2)
    video2 = myFilter.qs
    context = {"video2":video2, "myFilter":myFilter, "form2":form2, "all2":video2}
    
    return render(request, 'account/index.html', context)



@csrf_exempt    
def getInfo(request, tittle):
    add = Video.objects.get(id=tittle)
    adds = add.add_set.all()
    context = {'add':add, 'adds':adds}
    return render(request, 'account/getinfo.html', context)

@csrf_exempt    
def info(request, pk):
    form = Adding_form()
    if request.method == 'POST':
        form = Adding_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
            
       
    context = {'form':form}

    return render(request, 'account/companyinfo.html', context) 

def updateInfo(request, pk):
    adds = Add.objects.get(id=pk)
    form = Adding_form(instance=adds) 

    if request.method == 'POST':
        form = Adding_form(request.POST, instance=adds)
        if form.is_valid():
            form.save()
            return redirect('/')


    context = {'form':form}

    return render(request, 'account/companyinfo.html', context)

def aboutus(request):
    return render(request, 'account/aboutus.html')

@login_required(login_url='login')
def trending(request):
    return render(request, 'account/trending.html')

@login_required(login_url='Tshala:login')
def pitch(request):
    adds = Add.objects.all()
    all_video = Video.objects.all()
    form = Video_form()
    if request.method == "POST":
        form = Video_form(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = Video_form()
    
   
    context = {'form':form, 'all':all_video, 'adds':adds}

    return render(request, 'account/pitch.html', context)
      

def simpleCheckout(request):
    return render(request, 'account/simple_checkout.html')

def checkout(request, pk):
	video1 = Video.objects.get(id=pk)
	context = {'video1':video1}
	return render(request, 'account/checkout.html', context)




