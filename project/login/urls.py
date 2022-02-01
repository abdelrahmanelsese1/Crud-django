from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('', views.signup, name='signup'),
    path('logout/', views.mylogout, name="logout")
]