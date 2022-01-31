from django.shortcuts import render
from .models import student
# Create your views here.
def home(request):
    context = {}
    return render(request, 'home/mainpage.html', context)

def insertstudent(request):
        context = {}
        context['ID'] = 1
        if (request.method == 'GET'):
            return render(request, 'affairs/insertintake.html', context)
        else:

            # intsake reques.post
            print(request.POST)
            name = request.POST['studentName']
            email = request.POST['email']
            age = request.POST['age']
            track = request.POST['track']


            student.objects.create(name = name, age = age, email = email , track= track)
            intakes = student.objects.all()
            context['students'] = intakes
            context['msg'] = 'student inserted'
            return render(request, 'home/mainpage.html', context)
