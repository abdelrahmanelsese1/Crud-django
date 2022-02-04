from django import forms
from .models import Student, Track

class StudentInsert(forms.Form):
    fullname = forms.CharField(label='Name', max_length=30)
    age = forms.IntegerField(max_value=100)
    email = forms.EmailField(max_length=40)
    # trackid = forms.ChoiceField(choices=[(track.Trackid,track.trackname) for track in Track.objects.all()])

class AddStudent1(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
