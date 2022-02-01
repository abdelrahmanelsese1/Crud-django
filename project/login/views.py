from django.shortcuts import render , redirect
from .models import SignupInfo



# Create your views here.
def login(request):
    if (request.method=='GET'):
        return render(request,'login/login.html')
    else:
        user = SignupInfo.objects.filter(email=request.POST['email'], password=request.POST['password'])
        if (len(user) > 0):
            return redirect('/student/')
        else:
            context={}
            context['msg'] = 'invalid username or password'
            return render(request, 'login/login.html', context)

def signup(request):
    context = {}
    if (request.method == 'GET'):
        return render(request, 'login/signup.html', context)
    else:


        print(request.POST)


        SignupInfo.objects.create(username=request.POST['name'], email=request.POST['email'], password=request.POST['password'])
        signupinfos = SignupInfo.objects.all()
        context['SignupInfo'] = signupinfos
        context['msg'] = 'user inserted'
        return render(request, 'login/login.html', context)

