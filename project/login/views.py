from django.shortcuts import render , redirect, HttpResponseRedirect
from .models import SignupInfo
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as authlogin, logout


# Create your views here.
def mylogout(request):
    logout(request)
    return render(request, 'login/login.html')

def login(request):
    if request.method == 'GET':
        return render(request, 'login/login.html')
    else:
        user = SignupInfo.objects.filter(username=request.POST['username'], password=request.POST['password'])
        authuser = authenticate(username=request.POST['username'], password=request.POST['password'])

        if len(user) > 0 and authuser is not None:
            request.session['username'] = request.POST['username']
            authlogin(request, authuser)
            return HttpResponseRedirect('/home/student/')
        else:
            context={}
            context['msg'] = 'invalid username or password'
            return render(request, 'login/login.html', context)


def signup(request):
    context = {}
    if request.method == 'GET':
        return render(request, 'login/signup.html', context)
    else:

        SignupInfo.objects.create(username=request.POST['username'], email=request.POST['useremail'], password=request.POST['userpassword'])
        User.objects.create_user(username=request.POST['username'], password=request.POST['userpassword'], is_staff=True)

        return render(request, 'login/login.html', context)

