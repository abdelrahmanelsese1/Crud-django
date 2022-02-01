from django.shortcuts import render
from .models import SignupInfo

# Create your views here.
def login(request):
    context = {}
    return render(request, 'login/login.html', context)

def signup(request):
    context = {}
    context['ID'] = 1
    if (request.method == 'GET'):
        return render(request, 'login/signup.html', context)
    else:

        # intsake reques.post
        print(request.POST)
        name = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        SignupInfo.objects.create(name=name, email=email, password=password)
        signupinfos = SignupInfo.objects.all()
        context['SignupInfo'] = signupinfos
        context['msg'] = 'user inserted'
        return render(request, 'login/login.html', context)

