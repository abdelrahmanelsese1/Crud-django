from django.shortcuts import render
from .models import Student
from django.views import View
from .forms import AddStudent1

from .forms import StudentInsert
# Create your views here.
def home(request):
    context = {}
    return render(request, 'home/mainpage.html', context)

def insertstudent(request):
        context = {}
        context['ID'] = 1
        if request.method == 'GET':
            return render(request, 'home/mainpage.html', context)
        else:

            # intsake reques.post
            print(request.POST)
            name = request.POST['studentName']
            email = request.POST['email']
            age = request.POST['age']
            track = request.POST['track']

            Student.objects.create(name=name, age=age, email=email)
            students = Student.objects.all()
            context['students'] = students
            context['msg'] = 'student inserted'
            return render(request, 'home/mainpage.html', context)

def deletestudent(req,id):
    context = {}
    Student.objects.filter(id=id).delete()
    students = Student.objects.all()
    context['students'] = students
    return render(req, 'home/liststudent.html', context)

def liststudents(req):
    context={}
    students = Student.objects.all()
    context['students'] = students
    return render(req, 'home/liststudent.html', context)

def searchstudent(request):
    if request.method == 'GET':
        return render(request, 'home/search.html')
    else:
        search_name = Student.objects.filter(name=request.POST['search'])
        if len(search_name) > 0:
            request.session['searchName'] = request.POST['search']
            return render(request, 'home/search.html')
        else:
            request.session['error msg'] = 'No matching record'
            return render(request, 'home/search.html')

def updatestudent(request,id):
    if request.method == 'POST':
        username = request.POST.get('username')
        student = Student.objects.get(id=id)
        if student:
            student.name = username
            student.save()
            # students = Student.objects.all()
            # context = {'students': students}
            return render(request, 'home/mainpage.html')
        else:
            return render(request, 'home/liststudent.html')
    else:
        return render(request, 'home/liststudent.html')

class InsertStudent1(View):
    def get(self,request):
        print('class based get')
        context = {}
        form = AddStudent1()
        context['form'] = form
        return render(request, 'home/insertstudent.html', context)

    def post(self,request):
        print('class based post')
        context={}
        afterpostform = AddStudent1(request.POST)
        afterpostform.save()
        return render(request, 'home/insertstudent.html', context)




