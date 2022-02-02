from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('student/', views.insertstudent, name='student'),
    path('delete/<id>', views.deletestudent, name='delete'),
    path('list/', views.liststudents, name='list'),
    path('search/', views.searchstudent, name='search'),
    path('update/<id>', views.updatestudent, name='update'),
    path('insertstudent/', views.InsertStudent1.as_view(), name='insertstudent'),
]